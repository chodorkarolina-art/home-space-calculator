from decimal import Decimal

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ..models import Calculation


User = get_user_model()


class CalculationApiTest(APITestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(
            username="user1",
            password="test12345",
        )

        self.user2 = User.objects.create_user(
            username="user2",
            password="test12345",
        )

        self.user1_calculation = Calculation.objects.create(
            user=self.user1,
            name="Obliczenie użytkownika 1",
            adults=2,
            children=1,
            pets=0,
            remote_work=False,
            hobby=False,
            bikes=0,
            storage_level="medium",
            minimum_area=Decimal("50.00"),
            recommended_rooms=3,
            recommended_area=Decimal("55.00"),
            extra_room_recommendation=None,
            area_breakdown={},
        )

        self.user2_calculation = Calculation.objects.create(
            user=self.user2,
            name="Obliczenie użytkownika 2",
            adults=1,
            children=0,
            pets=1,
            remote_work=True,
            hobby=True,
            bikes=1,
            storage_level="large",
            minimum_area=Decimal("45.00"),
            recommended_rooms=2,
            recommended_area=Decimal("52.00"),
            extra_room_recommendation="Pokój wielofunkcyjny",
            area_breakdown={},
        )

    # NIEZALOGOWANY UŻYTKOWNIK NIE MA DOSTĘPU DO API
    def test_anonymous_user_cannot_access_calculations_api(self):
        response = self.client.get(
            reverse("api_calculations")
        )

        self.assertIn(
            response.status_code,
            [
                status.HTTP_401_UNAUTHORIZED,
                status.HTTP_403_FORBIDDEN,
            ],
        )

    # ZALOGOWANY UŻYTKOWNIK MA DOSTĘP DO API
    def test_authenticated_user_can_access_calculations_api(self):
        self.client.force_authenticate(
            user=self.user1
        )

        response = self.client.get(
            reverse("api_calculations")
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    # UŻYTKOWNIK WIDZI TYLKO SWOJE OBLICZENIA
    def test_user_sees_only_own_calculations(self):
        self.client.force_authenticate(
            user=self.user1
        )

        response = self.client.get(
            reverse("api_calculations")
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.assertEqual(
            len(response.data),
            1,
        )

        self.assertEqual(
            response.data[0]["id"],
            self.user1_calculation.id,
        )

        self.assertEqual(
            response.data[0]["name"],
            "Obliczenie użytkownika 1",
        )

    # API ZWRACA PODSTAWOWE DANE OBLICZENIA
    def test_api_returns_calculation_data(self):
        self.client.force_authenticate(
            user=self.user1
        )

        response = self.client.get(
            reverse("api_calculations")
        )

        calculation = response.data[0]

        self.assertEqual(
            calculation["adults"],
            2,
        )

        self.assertEqual(
            calculation["children"],
            1,
        )

        self.assertEqual(
            calculation["recommended_rooms"],
            3,
        )

        self.assertEqual(
            calculation["recommended_area"],
            "55.00",
        )
        
        # UŻYTKOWNIK MOŻE POBRAĆ SWOJĄ KALKULACJĘ PO ID

    def test_user_can_get_own_calculation_by_id(self):
        self.client.force_authenticate(
            user=self.user1
        )

        response = self.client.get(
            reverse(
                "api_calculation_detail",
                kwargs={
                    "pk": self.user1_calculation.id
                },
            )
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.assertEqual(
            response.data["id"],
            self.user1_calculation.id,
        )

        self.assertEqual(
            response.data["name"],
            "Obliczenie użytkownika 1",
        )


    # UŻYTKOWNIK NIE MOŻE POBRAĆ CUDZEJ KALKULACJI PO ID

    def test_user_cannot_get_other_users_calculation_by_id(self):
        self.client.force_authenticate(
            user=self.user1
        )

        response = self.client.get(
            reverse(
                "api_calculation_detail",
                kwargs={
                    "pk": self.user2_calculation.id
                },
            )
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND,
        )


    # NIEZALOGOWANY UŻYTKOWNIK NIE MA DOSTĘPU DO KALKULACJI PO ID

    def test_anonymous_user_cannot_get_calculation_by_id(self):
        response = self.client.get(
            reverse(
                "api_calculation_detail",
                kwargs={
                    "pk": self.user1_calculation.id
                },
            )
        )

        self.assertIn(
            response.status_code,
            [
                status.HTTP_401_UNAUTHORIZED,
                status.HTTP_403_FORBIDDEN,
            ],
        )
        
    # JWT - POPRAWNE DANE ZWRACAJĄ ACCESS I REFRESH

    def test_jwt_returns_access_and_refresh_tokens(self):
        response = self.client.post(
            reverse("token_obtain_pair"),
            {
                "username": "user1",
                "password": "test12345",
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)


    # JWT - ACCESS TOKEN DAJE DOSTĘP DO API

    def test_jwt_access_token_allows_api_access(self):
        token_response = self.client.post(
            reverse("token_obtain_pair"),
            {
                "username": "user1",
                "password": "test12345",
            },
            format="json",
        )

        access_token = token_response.data["access"]

        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {access_token}"
        )

        response = self.client.get(
            reverse("api_calculations")
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )


    # JWT - REFRESH TOKEN GENERUJE NOWY ACCESS TOKEN

    def test_jwt_refresh_token_returns_new_access_token(self):
        token_response = self.client.post(
            reverse("token_obtain_pair"),
            {
                "username": "user1",
                "password": "test12345",
            },
            format="json",
        )

        refresh_token = token_response.data["refresh"]

        response = self.client.post(
            reverse("token_refresh"),
            {
                "refresh": refresh_token,
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.assertIn("access", response.data)
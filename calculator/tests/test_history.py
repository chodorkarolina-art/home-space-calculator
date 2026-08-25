from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from ..models import Calculation


User = get_user_model()


class CalculationHistoryTest(TestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(
            username="user1",
            password="test12345",
        )

        self.user2 = User.objects.create_user(
            username="user2",
            password="test12345",
        )

        Calculation.objects.create(
            user=self.user1,
            name="Obliczenie użytkownika 1",
            adults=2,
            children=1,
            pets=0,
            remote_work=False,
            hobby=False,
            bikes=0,
            storage_level="medium",
            recommended_area=Decimal("50.00"),
        )

        Calculation.objects.create(
            user=self.user2,
            name="Obliczenie użytkownika 2",
            adults=1,
            children=0,
            pets=1,
            remote_work=True,
            hobby=True,
            bikes=1,
            storage_level="large",
            recommended_area=Decimal("48.00"),
        )

    # HISTORIA WYMAGA LOGOWANIA
    def test_history_requires_login(self):
        response = self.client.get(
            reverse("history")
        )

        self.assertEqual(
            response.status_code,
            302,
        )

    # UŻYTKOWNIK WIDZI TYLKO SWOJE OBLICZENIA
    def test_user_sees_only_own_calculations(self):
        self.client.login(
            username="user1",
            password="test12345",
        )

        response = self.client.get(
            reverse("history")
        )

        self.assertEqual(
            response.status_code,
            200,
        )

        calculations = response.context[
            "calculations"
        ]

        self.assertEqual(
            calculations.count(),
            1,
        )

        self.assertEqual(
            calculations.first().user,
            self.user1,
        )

    # UŻYTKOWNIK MOŻE OTWORZYĆ SZCZEGÓŁY SWOJEGO OBLICZENIA
    def test_user_can_open_own_calculation_detail(self):
        self.client.login(
            username="user1",
            password="test12345",
        )

        calculation = Calculation.objects.get(
            user=self.user1
        )

        response = self.client.get(
            reverse(
                "calculation_detail",
                args=[calculation.id],
            )
        )

        self.assertEqual(
            response.status_code,
            200,
        )

        self.assertEqual(
            response.context["calculation"],
            calculation,
        )

    # UŻYTKOWNIK NIE MOŻE OTWORZYĆ CUDZEGO OBLICZENIA
    def test_user_cannot_open_other_users_calculation(self):
        self.client.login(
            username="user1",
            password="test12345",
        )

        calculation = Calculation.objects.get(
            user=self.user2
        )

        response = self.client.get(
            reverse(
                "calculation_detail",
                args=[calculation.id],
            )
        )

        self.assertEqual(
            response.status_code,
            404,
        )

    # UŻYTKOWNIK MOŻE USUNĄĆ SWOJE OBLICZENIE
    def test_user_can_delete_own_calculation(self):
        self.client.login(
            username="user1",
            password="test12345",
        )

        calculation = Calculation.objects.get(
            user=self.user1
        )

        response = self.client.post(
            reverse(
                "calculation_delete",
                args=[calculation.id],
            )
        )

        self.assertEqual(
            response.status_code,
            302,
        )

        self.assertFalse(
            Calculation.objects.filter(
                id=calculation.id
            ).exists()
        )

    # UŻYTKOWNIK NIE MOŻE USUNĄĆ CUDZEGO OBLICZENIA
    def test_user_cannot_delete_other_users_calculation(self):
        self.client.login(
            username="user1",
            password="test12345",
        )

        calculation = Calculation.objects.get(
            user=self.user2
        )

        response = self.client.post(
            reverse(
                "calculation_delete",
                args=[calculation.id],
            )
        )

        self.assertEqual(
            response.status_code,
            404,
        )

        self.assertTrue(
            Calculation.objects.filter(
                id=calculation.id
            ).exists()
        )

    # UŻYTKOWNIK MOŻE EDYTOWAĆ SWOJE OBLICZENIE
    def test_user_can_edit_own_calculation(self):
        self.client.login(
            username="user1",
            password="test12345",
        )

        calculation = Calculation.objects.get(
            user=self.user1
        )

        response = self.client.post(
            reverse(
                "calculation_edit",
                args=[calculation.id],
            ),
            data={
                "name": "Edytowane obliczenie",
                "adults": 2,
                "children": 2,
                "pets": 1,
                "remote_work": True,
                "hobby": True,
                "bikes": 2,
                "storage_level": "large",
            },
        )

        self.assertEqual(
            response.status_code,
            302,
        )

        calculation.refresh_from_db()

        self.assertEqual(
            calculation.name,
            "Edytowane obliczenie",
        )

        self.assertEqual(
            calculation.children,
            2,
        )

        self.assertEqual(
            calculation.storage_level,
            "large",
        )

        self.assertIsNotNone(
            calculation.recommended_area
        )

    # UŻYTKOWNIK NIE MOŻE EDYTOWAĆ CUDZEGO OBLICZENIA
    def test_user_cannot_edit_other_users_calculation(self):
        self.client.login(
            username="user1",
            password="test12345",
        )

        calculation = Calculation.objects.get(
            user=self.user2
        )

        response = self.client.get(
            reverse(
                "calculation_edit",
                args=[calculation.id],
            )
        )

        self.assertEqual(
            response.status_code,
            404,
        )
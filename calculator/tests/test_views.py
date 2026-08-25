from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from ..models import Calculation


User = get_user_model()


class CalculatorViewTest(TestCase):

    # STRONA KALKULATORA DZIAŁA
    def test_calculator_page_works(self):
        response = self.client.get(
            reverse("calculator")
        )

        self.assertEqual(
            response.status_code,
            200,
        )

        self.assertTemplateUsed(
            response,
            "calculator/calculator_form.html",
        )

    # ZALOGOWANY UŻYTKOWNIK - ZAPIS DO BAZY
    def test_logged_user_calculation_is_saved(self):
        user = User.objects.create_user(
            username="karolina",
            password="test12345",
        )

        self.client.login(
            username="karolina",
            password="test12345",
        )

        response = self.client.post(
            reverse("calculator"),
            data={
                "name": "Testowe obliczenie",
                "adults": 2,
                "children": 1,
                "pets": 1,
                "remote_work": True,
                "hobby": False,
                "bikes": 2,
                "storage_level": "medium",
            },
        )

        self.assertEqual(
            response.status_code,
            302,
        )

        self.assertEqual(
            Calculation.objects.filter(
                user=user
            ).count(),
            1,
        )

    # NIEZALOGOWANY UŻYTKOWNIK - BRAK ZAPISU DO BAZY
    def test_anonymous_user_calculation_is_not_saved(self):
        response = self.client.post(
            reverse("calculator"),
            data={
                "name": "Testowe obliczenie",
                "adults": 2,
                "children": 1,
                "pets": 1,
                "remote_work": True,
                "hobby": False,
                "bikes": 2,
                "storage_level": "medium",
            },
        )

        self.assertEqual(
            response.status_code,
            302,
        )

        self.assertEqual(
            Calculation.objects.count(),
            0,
        )

    # PEŁNY PRZEPŁYW - FORMULARZ → WYNIKI
    def test_calculation_results_page_renders_after_post(self):
        user = User.objects.create_user(
            username="result_user",
            password="test12345",
        )

        self.client.login(
            username="result_user",
            password="test12345",
        )

        response = self.client.post(
            reverse("calculator"),
            data={
                "name": "Test wyniku",
                "adults": 2,
                "children": 1,
                "pets": 1,
                "remote_work": True,
                "hobby": True,
                "bikes": 2,
                "storage_level": "medium",
            },
            follow=True,
        )

        self.assertEqual(
            response.status_code,
            200,
        )

        self.assertTemplateUsed(
            response,
            "calculator/results.html",
        )

        self.assertContains(
            response,
            "Wynik obliczenia",
        )

        self.assertContains(
            response,
            "Test wyniku",
        )

        self.assertContains(
            response,
            "Edytuj obliczenie",
        )

        self.assertContains(
            response,
            "Usuń obliczenie",
        )

        self.assertContains(
            response,
            "Moje obliczenia",
        )
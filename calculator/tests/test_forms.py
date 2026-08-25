from django.test import TestCase

from ..forms import CalculationForm


class CalculationFormTest(TestCase):

    def test_calculation_form_is_valid(self):
        form = CalculationForm(
            data={
                "name": "Testowe obliczenie",
                "adults": 2,
                "children": 1,
                "pets": 1,
                "remote_work": True,
                "hobby": False,
                "bikes": 2,
                "storage_level": "medium",
            }
        )

        self.assertTrue(form.is_valid())
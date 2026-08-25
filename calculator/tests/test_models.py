from django.test import TestCase

from ..models import Calculation


class CalculationModelTest(TestCase):

    def test_create_calculation(self):
        calculation = Calculation.objects.create(
            adults=2,
            children=1,
            pets=1,
            remote_work=True,
            hobby=False,
            bikes=2,
            storage_level="medium",
        )

        self.assertEqual(calculation.adults, 2)
        self.assertEqual(calculation.children, 1)
        self.assertEqual(calculation.pets, 1)
        self.assertTrue(calculation.remote_work)
        self.assertFalse(calculation.hobby)
        self.assertEqual(calculation.bikes, 2)
        self.assertEqual(
            calculation.storage_level,
            "medium",
        )
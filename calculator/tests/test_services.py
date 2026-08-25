from decimal import Decimal

from django.test import TestCase

from ..services import (
    calculate_bathroom_area,
    calculate_bedroom_area,
    calculate_bikes_area,
    calculate_communication_area,
    calculate_dining_area,
    calculate_extra_room_recommendation,
    calculate_hobby_area,
    calculate_kitchen_area,
    calculate_living_dining_area,
    calculate_living_room_area,
    calculate_minimum_area,
    calculate_minimum_bedroom_area,
    calculate_pet_area,
    calculate_recommended_area,
    calculate_recommended_rooms,
    calculate_storage_adjustment,
    calculate_work_area,
)


class CalculationServiceTest(TestCase):

    # FUNKCJA OGÓLNA
    def test_calculate_recommended_area(self):
        result = calculate_recommended_area(
            adults=2,
            children=1,
            pets=1,
            remote_work=True,
            hobby=False,
            bikes=2,
            storage_level="medium",
        )

        self.assertEqual(
            result,
            Decimal("60.20"),
        )

    # MINIMUM
    def test_calculate_minimum_area_for_one_person(self):
        result = calculate_minimum_area(
            adults=1,
            children=0,
            storage_level="medium",
        )

        self.assertEqual(
            result,
            Decimal("36.20"),
        )

    # REKOMENDOWANA LICZBA POKOI
    def test_calculate_recommended_rooms(self):
        result = calculate_recommended_rooms(
            adults=2,
            children=1,
            remote_work=False,
        )

        self.assertEqual(
            result,
            3,
        )

    # DODATKOWA REKOMENDACJA - PRACA + HOBBY
    def test_extra_room_for_remote_work_and_hobby(self):
        result = calculate_extra_room_recommendation(
            remote_work=True,
            hobby=True,
        )

        self.assertEqual(
            result,
            "Gabinet / Pokój wielofunkcyjny",
        )

    # DODATKOWA REKOMENDACJA - PRACA
    def test_extra_room_for_remote_work(self):
        result = calculate_extra_room_recommendation(
            remote_work=True,
            hobby=False,
        )

        self.assertEqual(
            result,
            "Wydzielone miejsce do pracy",
        )

    # BRAK DODATKOWEJ REKOMENDACJI
    def test_no_extra_room_recommendation(self):
        result = calculate_extra_room_recommendation(
            remote_work=False,
            hobby=False,
        )

        self.assertIsNone(result)

    # SALON
    def test_calculate_living_room_area(self):
        result = calculate_living_room_area(
            adults=2,
            children=1,
        )

        self.assertEqual(
            result,
            Decimal("12.40"),
        )

    # JADALNIA
    def test_calculate_dining_area(self):
        result = calculate_dining_area(
            adults=2,
            children=2,
        )

        self.assertEqual(
            result,
            Decimal("4.00"),
        )

    # SALON + JADALNIA
    def test_calculate_living_dining_area(self):
        result = calculate_living_dining_area(
            adults=2,
            children=1,
        )

        self.assertEqual(
            result,
            Decimal("18.00"),
        )

    # KUCHNIA
    def test_calculate_kitchen_area(self):
        result = calculate_kitchen_area(
            storage_level="medium",
        )

        self.assertEqual(
            result,
            Decimal("7.00"),
        )

    # MINIMALNA POWIERZCHNIA SYPIALNI
    def test_calculate_minimum_bedroom_area(self):
        result = calculate_minimum_bedroom_area(
            adults=2,
            children=1,
        )

        self.assertEqual(
            result,
            Decimal("21.00"),
        )

    # SYPIALNIA
    def test_calculate_bedroom_area(self):
        result = calculate_bedroom_area(
            adults=2,
            children=1,
        )

        self.assertEqual(
            result,
            Decimal("21.00"),
        )

    # ŁAZIENKA
    def test_calculate_bathroom_area(self):
        result = calculate_bathroom_area()

        self.assertEqual(
            result,
            Decimal("4.30"),
        )

    # PRACA ZDALNA
    def test_calculate_work_area(self):
        result = calculate_work_area(
            remote_work=True,
        )

        self.assertEqual(
            result,
            Decimal("4.00"),
        )

    # PRZECHOWYWANIE - MAŁO
    def test_storage_adjustment_small(self):
        result = calculate_storage_adjustment(
            storage_level="small",
        )

        self.assertEqual(
            result,
            Decimal("-4.00"),
        )

    # PRZECHOWYWANIE - ŚREDNIO
    def test_storage_adjustment_medium(self):
        result = calculate_storage_adjustment(
            storage_level="medium",
        )

        self.assertEqual(
            result,
            Decimal("0.00"),
        )

    # PRZECHOWYWANIE - DUŻO
    def test_storage_adjustment_large(self):
        result = calculate_storage_adjustment(
            storage_level="large",
        )

        self.assertEqual(
            result,
            Decimal("4.00"),
        )

    # SPORT / HOBBY
    def test_calculate_hobby_area(self):
        result = calculate_hobby_area(
            hobby=True,
        )

        self.assertEqual(
            result,
            Decimal("3.00"),
        )

    # ROWERY
    def test_calculate_bikes_area(self):
        result = calculate_bikes_area(
            bikes=2,
        )

        self.assertEqual(
            result,
            Decimal("2.40"),
        )

    # BRAK ROWERÓW
    def test_calculate_bikes_area_without_bikes(self):
        result = calculate_bikes_area(
            bikes=0,
        )

        self.assertEqual(
            result,
            Decimal("0.00"),
        )

    # ZWIERZĘTA
    def test_calculate_pet_area(self):
        result = calculate_pet_area(
            pets=1,
        )

        self.assertEqual(
            result,
            Decimal("1.50"),
        )

    # KOMUNIKACJA
    def test_calculate_communication_area(self):
        result = calculate_communication_area(
            adults=2,
            children=2,
        )

        self.assertEqual(
            result,
            Decimal("2.50"),
        )
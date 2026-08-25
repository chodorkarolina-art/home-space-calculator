from django.shortcuts import render


def work_detail_view(request):
    context = {
        "title": "Praca zdalna",
        "description": (
            "Dodatkowa powierzchnia uwzględnia miejsce potrzebne "
            "do stworzenia wygodnego stanowiska pracy w domu."
        ),
        "elements": [
            "biurko",
            "krzesło",
            "miejsce na odsunięcie krzesła",
            "dostęp do stanowiska pracy",
        ],
        "area": "4.00",
    }

    return render(
        request,
        "calculator/additional/work.html",
        context,
    )


def hobby_detail_view(request):
    context = {
        "title": "Hobby / sport",
        "description": (
            "Powierzchnia zależy od dodatkowej przestrzeni potrzebnej "
            "na hobby, sport oraz przechowywanie sprzętu."
        ),
        "elements": [
            "miejsce do ćwiczeń lub realizowania hobby",
            "mata lub podstawowy sprzęt sportowy",
            "miejsce na sprzęt",
            "przestrzeń potrzebna do korzystania ze strefy",
        ],
        "area": "3.00",
    }

    return render(
        request,
        "calculator/additional/hobby.html",
        context,
    )


def bikes_detail_view(request):
    context = {
        "title": "Rowery",
        "description": (
            "Rowery wymagają dodatkowego miejsca do przechowywania "
            "oraz swobodnego dostępu."
        ),
        "elements": [
            "miejsce na rower",
            "dostęp do roweru",
            "podstawowa przestrzeń potrzebna do przechowywania",
        ],
        "area_per_bike": "1.20",
    }

    return render(
        request,
        "calculator/additional/bikes.html",
        context,
    )


def pets_detail_view(request):
    context = {
        "title": "Zwierzęta",
        "description": (
            "Dodatkowa powierzchnia uwzględnia podstawowe potrzeby "
            "zwierzęcia i jego wyposażenie."
        ),
        "elements": [
            "legowisko",
            "miski",
            "drapak lub inne wyposażenie",
            "miejsce na podstawowe akcesoria",
        ],
        "area_per_pet": "1.50",
    }

    return render(
        request,
        "calculator/additional/pets.html",
        context,
    )


def storage_detail_view(request):
    context = {
        "title": "Przechowywanie",
        "description": (
            "Poziom średni jest wartością bazową algorytmu. "
            "Mała ilość rzeczy zmniejsza rekomendowaną powierzchnię, "
            "a duża ilość rzeczy ją zwiększa."
        ),
        "small_adjustment": "-4.00",
        "medium_adjustment": "0.00",
        "large_adjustment": "+4.00",
    }

    return render(
        request,
        "calculator/additional/storage.html",
        context,
    )
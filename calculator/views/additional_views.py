from django.shortcuts import render

from ..additional_data import ADDITIONAL_DETAILS


def work_detail_view(request):
    return render(
        request,
        "calculator/additional/work.html",
        ADDITIONAL_DETAILS["work"],
    )


def hobby_detail_view(request):
    return render(
        request,
        "calculator/additional/hobby.html",
        ADDITIONAL_DETAILS["hobby"],
    )


def bikes_detail_view(request):
    return render(
        request,
        "calculator/additional/bikes.html",
        ADDITIONAL_DETAILS["bikes"],
    )


def pets_detail_view(request):
    return render(
        request,
        "calculator/additional/pets.html",
        ADDITIONAL_DETAILS["pets"],
    )


def storage_detail_view(request):
    return render(
        request,
        "calculator/additional/storage.html",
        ADDITIONAL_DETAILS["storage"],
    )
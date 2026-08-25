from django.shortcuts import render

from ..room_data import ROOM_DETAILS


def living_room_detail_view(request):
    context = ROOM_DETAILS["living_room"]

    return render(
        request,
        "calculator/rooms/living_room.html",
        context,
    )


def kitchen_detail_view(request):
    context = ROOM_DETAILS["kitchen"]

    return render(
        request,
        "calculator/rooms/kitchen.html",
        context,
    )


def bedroom_detail_view(request):
    context = ROOM_DETAILS["bedroom"]

    return render(
        request,
        "calculator/rooms/bedroom.html",
        context,
    )


def bathroom_detail_view(request):
    context = ROOM_DETAILS["bathroom"]

    return render(
        request,
        "calculator/rooms/bathroom.html",
        context,
    )
from django.shortcuts import redirect, render

from ..forms import CalculationForm
from ..models import Calculation
from ..services import (
    calculate_area_breakdown,
    calculate_extra_room_recommendation,
    calculate_minimum_area,
    calculate_recommended_area,
    calculate_recommended_rooms,
)


def home_view(request):
    return render(
        request,
        "calculator/home.html",
    )


def calculator_view(request):
    if request.method == "POST":
        form = CalculationForm(request.POST)

        if form.is_valid():
            minimum_area = calculate_minimum_area(
                adults=form.cleaned_data["adults"],
                children=form.cleaned_data["children"],
                storage_level=form.cleaned_data["storage_level"],
            )

            recommended_area = calculate_recommended_area(
                adults=form.cleaned_data["adults"],
                children=form.cleaned_data["children"],
                pets=form.cleaned_data["pets"],
                remote_work=form.cleaned_data["remote_work"],
                hobby=form.cleaned_data["hobby"],
                bikes=form.cleaned_data["bikes"],
                storage_level=form.cleaned_data["storage_level"],
            )

            recommended_rooms = calculate_recommended_rooms(
                adults=form.cleaned_data["adults"],
                children=form.cleaned_data["children"],
                remote_work=form.cleaned_data["remote_work"],
            )

            extra_room_recommendation = (
                calculate_extra_room_recommendation(
                    remote_work=form.cleaned_data["remote_work"],
                    hobby=form.cleaned_data["hobby"],
                )
            )

            area_breakdown = calculate_area_breakdown(
                adults=form.cleaned_data["adults"],
                children=form.cleaned_data["children"],
                pets=form.cleaned_data["pets"],
                remote_work=form.cleaned_data["remote_work"],
                hobby=form.cleaned_data["hobby"],
                bikes=form.cleaned_data["bikes"],
                storage_level=form.cleaned_data["storage_level"],
            )

            request.session["calculation_result"] = {
                "name": form.cleaned_data["name"],
                "minimum_area": str(minimum_area),
                "recommended_area": str(recommended_area),
                "recommended_rooms": recommended_rooms,
                "extra_room_recommendation": extra_room_recommendation,
                "area_breakdown": {
                    key: str(value)
                    for key, value in area_breakdown.items()
                },
            }

            if request.user.is_authenticated:
                Calculation.objects.create(
                    user=request.user,
                    name=form.cleaned_data["name"],
                    adults=form.cleaned_data["adults"],
                    children=form.cleaned_data["children"],
                    pets=form.cleaned_data["pets"],
                    remote_work=form.cleaned_data["remote_work"],
                    hobby=form.cleaned_data["hobby"],
                    bikes=form.cleaned_data["bikes"],
                    storage_level=form.cleaned_data["storage_level"],
                    minimum_area=minimum_area,
                    recommended_rooms=recommended_rooms,
                    recommended_area=recommended_area,
                )

            return redirect("results")

    else:
        form = CalculationForm()

    return render(
        request,
        "calculator/calculator_form.html",
        {
            "form": form,
        },
    )
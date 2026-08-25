from django.contrib.auth.decorators import login_required
from django.shortcuts import (
    get_object_or_404,
    redirect,
    render,
)

from ..additional_data import ADDITIONAL_DETAILS
from ..forms import CalculationForm
from ..models import Calculation
from ..room_data import ROOM_DETAILS
from ..services import (
    calculate_area_breakdown,
    calculate_extra_room_recommendation,
    calculate_minimum_area,
    calculate_recommended_area,
    calculate_recommended_rooms,
)


@login_required
def history_view(request):
    calculations = (
        Calculation.objects
        .filter(user=request.user)
        .order_by("-created_at")
    )

    return render(
        request,
        "calculator/history.html",
        {
            "calculations": calculations,
        },
    )


@login_required
def calculation_detail_view(request, calculation_id):
    calculation = get_object_or_404(
        Calculation,
        id=calculation_id,
        user=request.user,
    )

    return render(
        request,
        "calculator/calculation_detail.html",
        {
            "calculation": calculation,
            "room_details": ROOM_DETAILS,
            "additional_details": ADDITIONAL_DETAILS,
        },
    )


@login_required
def calculation_edit_view(request, calculation_id):
    calculation = get_object_or_404(
        Calculation,
        id=calculation_id,
        user=request.user,
    )

    if request.method == "POST":
        form = CalculationForm(
            request.POST,
            instance=calculation,
        )

        if form.is_valid():
            updated_calculation = form.save(
                commit=False
            )

            minimum_area = calculate_minimum_area(
                adults=form.cleaned_data["adults"],
                children=form.cleaned_data["children"],
                storage_level=form.cleaned_data["storage_level"],
            )

            recommended_rooms = calculate_recommended_rooms(
                adults=form.cleaned_data["adults"],
                children=form.cleaned_data["children"],
                remote_work=form.cleaned_data["remote_work"],
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

            serialized_breakdown = {
                key: str(value)
                for key, value in area_breakdown.items()
            }

            updated_calculation.minimum_area = minimum_area
            updated_calculation.recommended_rooms = recommended_rooms
            updated_calculation.recommended_area = recommended_area

            updated_calculation.extra_room_recommendation = (
                extra_room_recommendation
            )

            updated_calculation.area_breakdown = (
                serialized_breakdown
            )

            updated_calculation.user = request.user

            updated_calculation.save()

            return redirect(
                "calculation_detail",
                calculation_id=updated_calculation.id,
            )

    else:
        form = CalculationForm(
            instance=calculation,
        )

    return render(
        request,
        "calculator/calculation_edit.html",
        {
            "form": form,
            "calculation": calculation,
        },
    )


@login_required
def calculation_delete_view(request, calculation_id):
    calculation = get_object_or_404(
        Calculation,
        id=calculation_id,
        user=request.user,
    )

    if request.method == "POST":
        calculation.delete()

        return redirect(
            "history"
        )

    return render(
        request,
        "calculator/calculation_delete.html",
        {
            "calculation": calculation,
        },
    )
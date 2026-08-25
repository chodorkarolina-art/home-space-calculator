from django.contrib.auth.decorators import login_required
from django.shortcuts import (
    get_object_or_404,
    redirect,
    render,
)

from ..forms import CalculationForm
from ..models import Calculation
from ..services import (
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

            updated_calculation.minimum_area = (
                calculate_minimum_area(
                    adults=form.cleaned_data["adults"],
                    children=form.cleaned_data["children"],
                    storage_level=form.cleaned_data["storage_level"],
                )
            )

            updated_calculation.recommended_rooms = (
                calculate_recommended_rooms(
                    adults=form.cleaned_data["adults"],
                    children=form.cleaned_data["children"],
                    remote_work=form.cleaned_data["remote_work"],
                )
            )

            updated_calculation.recommended_area = (
                calculate_recommended_area(
                    adults=form.cleaned_data["adults"],
                    children=form.cleaned_data["children"],
                    pets=form.cleaned_data["pets"],
                    remote_work=form.cleaned_data["remote_work"],
                    hobby=form.cleaned_data["hobby"],
                    bikes=form.cleaned_data["bikes"],
                    storage_level=form.cleaned_data["storage_level"],
                )
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
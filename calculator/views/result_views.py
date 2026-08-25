from decimal import Decimal

from django.shortcuts import redirect, render


def results_view(request):
    result = request.session.get("calculation_result")

    if not result:
        return redirect("calculator")

    area_breakdown = {
        key: Decimal(value)
        for key, value in result["area_breakdown"].items()
    }

    context = {
        "name": result.get("name"),
        "minimum_area": Decimal(result["minimum_area"]),
        "recommended_area": Decimal(result["recommended_area"]),
        "recommended_rooms": result["recommended_rooms"],
        "extra_room_recommendation": result.get(
            "extra_room_recommendation"
        ),
        "area_breakdown": area_breakdown,
        "calculation_id": result.get("calculation_id"),
    }

    return render(
        request,
        "calculator/results.html",
        context,
    )
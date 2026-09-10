from django.urls import path

from .views import (
    CalculationDetailAPIView,
    CalculationListAPIView,
)


urlpatterns = [
    path(
        "calculations/",
        CalculationListAPIView.as_view(),
        name="api_calculations",
    ),

    path(
        "calculations/<int:pk>/",
        CalculationDetailAPIView.as_view(),
        name="api_calculation_detail",
    ),
]
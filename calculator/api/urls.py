from django.urls import path

from .views import CalculationListAPIView


urlpatterns = [
    path(
        "calculations/",
        CalculationListAPIView.as_view(),
        name="api_calculations",
    ),
]
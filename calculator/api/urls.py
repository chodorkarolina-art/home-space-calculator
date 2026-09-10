from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

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

    path(
        "token/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),

    path(
        "token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh",
    ),
]
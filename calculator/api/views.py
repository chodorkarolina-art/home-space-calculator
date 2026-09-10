from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ..models import Calculation
from .serializers import CalculationSerializer


class CalculationListAPIView(generics.ListAPIView):
    serializer_class = CalculationSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(self):
        return (
            Calculation.objects
            .filter(user=self.request.user)
            .order_by("-created_at")
        )
        
class CalculationDetailAPIView(generics.RetrieveAPIView):
    serializer_class = CalculationSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(self):
        return Calculation.objects.filter(
            user=self.request.user
        )
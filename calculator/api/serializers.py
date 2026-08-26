from rest_framework import serializers

from ..models import Calculation


class CalculationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calculation

        fields = [
            "id",
            "name",
            "adults",
            "children",
            "pets",
            "remote_work",
            "hobby",
            "bikes",
            "storage_level",
            "minimum_area",
            "recommended_rooms",
            "recommended_area",
            "extra_room_recommendation",
            "area_breakdown",
            "created_at",
        ]
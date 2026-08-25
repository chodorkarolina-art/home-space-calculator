from django.conf import settings
from django.db import models


class Calculation(models.Model):
    STORAGE_CHOICES = [
        ("small", "Mało"),
        ("medium", "Średnio"),
        ("large", "Dużo"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="calculations",
    )

    name = models.CharField(
        max_length=120,
        default="Moje obliczenie",
    )

    adults = models.PositiveIntegerField(default=1)
    children = models.PositiveIntegerField(default=0)
    pets = models.PositiveIntegerField(default=0)

    remote_work = models.BooleanField(default=False)
    hobby = models.BooleanField(default=False)

    bikes = models.PositiveIntegerField(default=0)

    storage_level = models.CharField(
        max_length=10,
        choices=STORAGE_CHOICES,
        default="medium",
    )
    
    minimum_area = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True,
    )

    recommended_rooms = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    recommended_area = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
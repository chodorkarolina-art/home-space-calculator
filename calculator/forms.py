from django import forms

from .models import Calculation


class CalculationForm(forms.ModelForm):

    class Meta:
        model = Calculation

        fields = [
            "name",
            "adults",
            "children",
            "pets",
            "remote_work",
            "hobby",
            "bikes",
            "storage_level",
        ]

        labels = {
            "name": "Nazwa obliczenia",
            "adults": "Dorośli",
            "children": "Dzieci",
            "pets": "Zwierzęta",
            "remote_work": "Praca zdalna",
            "hobby": "Hobby / sport",
            "bikes": "Liczba rowerów",
            "storage_level": "Ilość rzeczy do przechowywania",
        }

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Np. Mieszkanie dla rodziny 2+1",
                }
            ),
        }
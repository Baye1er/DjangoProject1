from django import forms
from .models import Formulaire



class FormulaireForm(forms.ModelForm):
    class Meta:
        model = Formulaire
        fields = "__all__"

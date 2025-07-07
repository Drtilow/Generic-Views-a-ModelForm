from django import forms
from .models import Jacket

class JacketForm(forms.ModelForm):
    class Meta:
        model = Jacket
        fields = ['brand', 'color']

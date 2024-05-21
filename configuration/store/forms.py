from django import forms
from configuration.models import Store
class StoreForm(forms.ModelForm):
    class Meta:
        model=Store
        fields="__all__"

from django import forms
from configuration.models import Items_type
class Item_typeForm(forms.ModelForm):
    class Meta:
        model=Items_type
        fields="__all__"

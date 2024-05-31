from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from configuration.models import Items
class ItemsForm(forms.ModelForm):
    def __init__(self, *args,**kwargs):
        super(ItemsForm,self).__init__( *args,**kwargs)
        self.fields['unit'].widget.attrs.update({
            'class':'formset-field form-control' })
        self.fields['items_type'].widget.attrs.update({
            'class':'formset-field form-control' })
        self.fields['barcode'].widget.attrs.update({
            'class':'formset-field form-control' })
        self.fields['name_lo'].widget.attrs.update({
            'class':'formset-field form-control' })
        self.fields['name_fk'].widget.attrs.update({
            'class':'formset-field form-control' })
    class Meta:
        model=Items
        fields="__all__"

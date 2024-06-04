from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from purchases.models import Supplier
class SupplierForm(forms.ModelForm):
    def __init__(self, *args,**kwargs):
        super(SupplierForm,self).__init__( *args,**kwargs)
        self.fields['name_lo'].widget.attrs.update({
            'class':'formset-field form-control' })
        self.fields['name_fk'].widget.attrs.update({
            'class':'formset-field form-control' })
        self.fields['phone'].widget.attrs.update({
            'class':'formset-field form-control' })
        self.fields['is_stop'].widget.attrs.update({
            'class':'formset-field form-control' })
    class Meta:
        model=Supplier
        fields="__all__"
        execute='created'


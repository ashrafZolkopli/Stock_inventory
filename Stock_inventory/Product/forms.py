from django import forms
from django.db.models import fields
from django.forms import inlineformset_factory
from .models import (
    ProductImage,
    Supplier,
    Product,
    Stock
)


class SupplierCreateForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = [
            'company_name',
            'address',
            'contact_person',
            'contact_no'
        ]


class SupplierUpdateForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = [
            'address',
            'contact_person',
            'contact_no'
        ]


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'spec',
        ]


class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'spec',
        ]


ProductImageInlineFormSet = inlineformset_factory(
    Product,
    ProductImage,
    fields=[
        'image_name',
        'description',
        'image'
    ]
)


class StockCreateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = [
            'quantity'
        ]

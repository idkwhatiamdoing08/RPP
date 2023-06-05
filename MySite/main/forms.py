from .models import Items
from django.forms import ModelForm, TextInput


class ItemsForm(ModelForm):
    class Meta:
        model = Items
        fields = ['vendor_code', 'name', 'price']

        widgets = {
            "vendor_code": TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Артикул'
            }),
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название товара'
            }),
            "price": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена'
            }),
        }

from django import forms
from django.forms import ModelForm
from .models import Item

class ItemForm(ModelForm):

    class Meta:
        model = Item
        fields = ['name', 'category', 'quantity', 'memo']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '例）シャープペンシル'
            }),
            'category': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '例）筆記具'
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0,
            }),
            'memo': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'メモ',
            }),
        }

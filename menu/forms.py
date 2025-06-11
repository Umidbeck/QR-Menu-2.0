from django import forms
from .models import Product, Category

class ProductForm(forms.ModelForm):
    """Form for creating and updating products"""
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category', 'image', 'available']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'available': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
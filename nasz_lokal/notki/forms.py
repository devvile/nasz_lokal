from django import forms
from .models import Category

class AddCat(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
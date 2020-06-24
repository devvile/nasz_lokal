from django import forms
from .models import Category, Wpis

class AddCat(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']



class AddNote(forms.ModelForm):
    class Meta:
        model = Wpis
        fields = ['name','note']
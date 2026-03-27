from django import forms
from .models import Category, Phones


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', ]


class Phone(forms.ModelForm):
    class Meta:
        model = Phones
        fields = "__all__"

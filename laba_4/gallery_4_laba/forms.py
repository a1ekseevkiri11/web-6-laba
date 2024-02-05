from django import forms
from .models import Cat

class ImageForm(forms.ModelForm):
    class Meta:
        model = Cat
        fields = ['photo', 'description']
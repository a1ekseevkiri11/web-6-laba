from django import forms
from .models import Product

class ImageForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class CaptchaForm(forms.Form):
    key = forms.CharField(widget=forms.HiddenInput())
    answer = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'autocomplete': 'off'}))
from django import forms
from django.core.validators import MaxLengthValidator
from django.core import validators


class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        'class':'form-control'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control'
    }))
    message = forms.CharField(validators=[MaxLengthValidator(300)], widget=forms.Textarea(attrs={
        'class': 'md-textarea'
    }))



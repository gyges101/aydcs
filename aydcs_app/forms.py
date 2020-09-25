from django import forms
from django.forms import ModelForm
from .models import info, essai

class infoRecu(ModelForm):
    class Meta:
        model = info
        fields = '__all__'

class essaiRecu(ModelForm):
    class Meta:
        model = essai
        fields = '__all__'
from dataclasses import fields
from django.forms import ModelForm
from .models import help

class HelpForm(ModelForm):
    class Meta:
        model = help
        fields = ['tille', 'body']

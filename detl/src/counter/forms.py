from django import forms

from .models import click

class clickForm(forms.ModelForm):
    class Meta:
        model = click
        fields = []
from django.db import models
from django import forms


class GetEarnings(forms.Form):
    ticker = forms.CharField(max_length=5)
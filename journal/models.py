from django.db import models
from django import forms


class Stock(models.Model):
    company = models.CharField(max_length=255)
    ticker = models.CharField(max_length=5)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sector = models.CharField(max_length=30)

class EarningReport(models.Model):
    report_date = models.DateTimeField()
    eps = models.DecimalField(max_digits=6, decimal_places=2)
    revenue = models.DecimalField(max_digits=6, decimal_places=2)
    eps_forecast = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, null=True)

class NewsArticle(models.Model):
    headline = models.CharField(max_length=255)
    content = models.TextField(null=True)
    source = models.CharField(max_length=255)
    publication_date = models.DateTimeField()
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, null=True)

class GetEarnings(forms.Form):
    ticker = forms.CharField(max_length=5)
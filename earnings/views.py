from django.shortcuts import render
from journal.models import GetEarnings
from django.shortcuts import render
from . import models
from bs4 import BeautifulSoup
import requests
from django.http import HttpResponse
from django.http import HttpResponse

def earnings_view(request):
    form = GetEarnings
    if request.method == 'POST':
        form = GetEarnings(request.POST)
        if form.is_valid():
            ticker = form.cleaned_data['ticker']
            url = f'https://www.earningswhispers.com/epsdetails/{ticker}'
            result = requests.get(url)
            doc = BeautifulSoup(result.text, 'html.parser')
            doc.prettify()
            eps = doc.find_all(class_='mainitem')

            eps_estimate = doc.find_all(class_='thirditem')

            revenue = doc.find_all(class_='fourthitem')

            return render(request, 'earningsoutput.html', {'eps': eps[0].string,
                                                           'eps_estimate': eps_estimate[0].string,
                                                           'revenue': revenue[0].string},)
    return render(request, 'earningsform.html', {'form': form})


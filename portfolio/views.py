from django.shortcuts import render
from .models import Portfolio
# Create your views here.

def portFo(request):
    portfolios = Portfolio.objects
    return render(request, 'portFo.html', {'portfolios' : portfolios})
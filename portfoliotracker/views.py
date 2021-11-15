from django.shortcuts import render
#from yahoo_fin.stock_info import *
import requests
from .models import Position
# Create your views here.
def index(request):
    data=Position.objects.all()

    context = {'data': data}

    return render(request, 'index.html', context)








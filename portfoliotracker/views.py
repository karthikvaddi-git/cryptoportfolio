from django.shortcuts import render,HttpResponse
from rest_framework.response import Response
#from yahoo_fin.stock_info import *
import requests
from channels.layers import get_channel_layer
import json
from .models import Position
from django.http import JsonResponse
# Create your views here.

from django.core import serializers


def index(request):
    data=Position.objects.all()

    context = {'data': data}

    return render(request, 'index.html', context)

from asgiref.sync import async_to_sync
def test(request):
    channel_layer = get_channel_layer()
    print("test ccalled in test function")

    data = Position.objects.all()

    print("\n")



    x = serializers.serialize("json", data)
    print("printing x in django ")
    print("\n")
    print(x)



    async_to_sync(channel_layer.group_send)(
        "checking",
        {
            'type': 'send_notification',
            'message': x
        }
    )
    return HttpResponse("Done")






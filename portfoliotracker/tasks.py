from django.contrib.auth import get_user_model
from portfolio import settings
from celery import shared_task
from celery import shared_task
from .models import Test, Position

#from .utils import get_random_code

#from celery.decorators import periodic_task
#from celery.task.schedules import crontab
import requests


@shared_task
def get_crypto_data():
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=INR&order=market_cap_desc&per_page=100&page=1&sparkline=false'
    data = requests.get(url).json()
    print("hello in shared task from ask")

""""
    for item in data:
        p, _ = Position.objects.get_or_create(name=item['name'])
        p.image = item['image']
        p.price = item['current_price']
        p.rank = item['market_cap_rank']
        p.market_cap = item['market_cap']
        p.save()
"""


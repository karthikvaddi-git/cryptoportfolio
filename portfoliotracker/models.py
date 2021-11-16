from django.db import models
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
# Create your models here.
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
from django.core import serializers

class Test(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return str(self.id)


class Position(models.Model):
    name = models.CharField(max_length=200)
    image = models.URLField()
    price = models.CharField(max_length=200)
    rank = models.CharField(max_length=10)
    market_cap = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)


def postsavemethod(sender,instance,created,**kwargs):

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


post_save.connect(postsavemethod, sender=Position)

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

# Guest -- Movie -- Reservation
class Movies(models.Model):
    hall = models.CharField(max_length=10)
    movie = models.CharField(max_length=10)
    # date = models.DateField()

    def __str__(self):
        return self.hall



class Guest(models.Model):
    name = models.CharField(max_length=20)
    mobile = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    guest = models.ForeignKey(Guest,on_delete=models.CASCADE, related_name='reservation')
    movie = models.ForeignKey(Movies,on_delete=models.CASCADE, related_name='reservation')

    def __str__(self):
        return self.guest.name
    

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)

    body = models.TextField(max_length=50)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def TokenCreate(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)
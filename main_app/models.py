from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Current_Balance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    amount = models.FloatField()

    def get_absolute_url(self):
        return reverse('home')
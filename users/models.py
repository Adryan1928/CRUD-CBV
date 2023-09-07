from django.db import models
from django.contrib.auth.models import User

class Suporte(models.Model):
    name = models.CharField(max_length=30)
    usuario = models.OneToOneField(User, on_delete=models.SET_NULL, blank=True, null=True) #models.SET_NULL models.PROTECT

    def __str__(self):
        return self.name

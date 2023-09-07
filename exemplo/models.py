from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(blank=True, null=True) #Tenho que estudar essa parte(Já estudei)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=False, blank=False, related_name="clientes")

    def __str__(self):
        return self.name
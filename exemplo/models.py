from django.db import models

class Cliente(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(blank=True, null=True) #Tenho que estudar essa parte

    def __str__(self):
        return self.name
from django.db import models

class Car(models.Model):
    # Add manager with another name
    brand = models.CharField(max_length=120)
    model = models.IntegerField()
    comercialValue = models.IntegerField()
    dialyValue = models.IntegerField()
    allow = models.BooleanField()

    objects = models.Manager()

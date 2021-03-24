from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager


class Car(AbstractBaseUser,models.Model):
    _id = models.IntegerField(unique = True)
    brand = models.TextField()
    model = models.TextField()
    comercial_value = models.FloatField()
    dialy_alquiler_value = models.FloatField()
    allow = models.BooleanField()

    USERNAME_FIELD = '_id'
    REQUIRED_FIELDS = ['brand','model','comercial_value','dialy_alquiler_value','allow']

    objects =  UserManager()

    def __str__(self):
        return str(self._id)
    

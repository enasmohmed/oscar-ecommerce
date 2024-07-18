from django.db import models

# Create your models here.
from oscar.apps.address.models import Country


class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)


    def __str__(self):
        return self.name



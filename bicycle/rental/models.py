from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Location(models.Model):
    loc_name = models.CharField(max_length = 200)

    def __str__(self):
        return self.loc_name


class Cycle(models.Model):
    cycle_num = models.IntegerField()
    location = models.ForeignKey('Location',on_delete=models.CASCADE)

    


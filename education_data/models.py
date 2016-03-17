from __future__ import unicode_literals
from django.db import models


class People(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Education(models.Model):
    education = models.CharField(max_length=20)
    people = models.ManyToManyField(People)

    def __unicode__(self):
        return self.education

class CurrencyList(models.Model):
    cur_short_name = models.CharField(max_length=3)
    
    def __unicode__(self):
        return self.cur_short_name

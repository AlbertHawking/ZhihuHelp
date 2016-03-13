from __future__ import unicode_literals

from django.db import models

# Create your models here.
class LoginRecord(models.Model):
    account    = models.CharField(max_length=200, unique=True)
    password   = models.CharField(max_length=200)
    recordDate = models.DateField(auto_now=True)
    cookie     = models.TextField()

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.account
    
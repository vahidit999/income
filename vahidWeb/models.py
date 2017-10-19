from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models



# Create your models here.
class Expense(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User)
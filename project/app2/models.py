from django.db import models

from django.db import models

class People(models.Model):
    fname = models.CharField(max_length = 50)
    lname = models.CharField(max_length = 50)
    age = models.IntegerField()
    sex = models.CharField(max_length=20, null=True)
    hobby = models.CharField(max_length=100, null=True)



from django.db import models

class StudentModel(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    contact = models.IntegerField(unique=True)
    gender = models.CharField(max_length=10)
    username = models.CharField(max_length=20,unique=True)


class LoginModel(models.Model):
    username = models.CharField(max_length=20,unique=True)
    password = models.CharField(max_length=20)
    type = models.CharField(max_length=10)


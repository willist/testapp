from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=200)
    phone = models.IntegerField()
    email = models.EmailField()

class Business(models.Model):
    name = models.CharField(max_length=200)
    contacts = models.ManyToManyField(Contact)

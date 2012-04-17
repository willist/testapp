from django.db import models
from django.core.validators import validate_email
from bizapp.validators import validate_phone

class Business(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20, validators=[validate_phone])
    email = models.EmailField(validators=[validate_email])
    business = models.ForeignKey(Business)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    business = models.ForeignKey(Business)



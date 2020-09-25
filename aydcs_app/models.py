from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class info(models.Model):

    nom = models.CharField(max_length=150)
    email = models.EmailField(max_length=200)
    sujet = models.CharField(max_length=500)
    message = models.TextField(max_length=4500)
    temps = models.CharField(max_length=100)

    def __str__(self):
        return str(self.nom)


class essai(models.Model):

    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=50)
    cours = models.CharField(max_length=20)
    timesend = models.CharField(max_length=60)
    def __str__(self):
        return str(self.nom)
    

class coursVa(models.Model):
    coursValid = models.CharField(max_length=40)
    def __str__(self):
        return str(self.coursValid)
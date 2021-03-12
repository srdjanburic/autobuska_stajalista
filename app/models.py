from django.db import models
from django.forms import ModelForm
from django.shortcuts import reverse


class Stanica(models.Model):
    naziv = models.CharField(max_length=200)
    opis = models.CharField(max_length=200)
    tacka = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.naziv}"

    def get_absolute_url(self):
        return reverse('app:stanice')

class Linija(models.Model):
    naziv=models.CharField(max_length=200)
  
    
    stanice = models.ManyToManyField(Stanica, related_name='stanica')
    
    def __str__ (self):
        return f"{self.naziv}"

    def get_absolute_url(self):
        return reverse('app:linije')


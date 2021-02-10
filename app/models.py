from django.db import models
from django.shortcuts import reverse


class Stanica(models.Model):
    naziv = models.CharField(max_length=200)
    opis = models.CharField(max_length=200)
    tacka = models.CharField(max_length=100)

    def __str__(self):
        return f"Naziv: {self.naziv}, Opis: {self.opis}, Pozicija: ({self.tacka})"

    def get_absolute_url(self):
        return reverse('app:stanice')

class Linija(models.Model):
    naziv=models.CharField(max_length=200)
    broj_stanica = models.IntegerField(default=0)
    

    stanice = models.ManyToManyField(Stanica) 

    def __str__ (self):
        return f"{self.naziv} {self.broj_stanica}"

    def get_absolute_url(self):
        return reverse('app:linije')

    


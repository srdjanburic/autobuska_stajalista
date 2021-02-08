from django.db import models
from django.shortcuts import reverse


class Stanica(models.Model):
    naziv = models.CharField(max_length=200)
    opis = models.CharField(max_length=200)
    tacka = models.CharField(max_length=100)

    def __str__(self):
        return f"Naziv: {self.naziv}, Opis: {self.opis}, Pozicija: ({self.tacka})"

    def get_absolute_url(self):
        return reverse('stanice')



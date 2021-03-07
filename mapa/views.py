from django.shortcuts import render
from django.core import serializers
from app.models import Stanica, Linija
from django.http import HttpResponse
import json

def mapa(request):    
    return render(request, 'mapa/index.html')

def mapa_linija_prikaz(request, pk):
    linija = Linija.objects.get(pk=pk)
    
    return render(request, 'mapa/linija.html', {'linija':linija, 'pk':pk})

def mapa_stanice(request):
     stanice = Stanica.objects.all()
     data = serializers.serialize('json',stanice)
     return HttpResponse(data, content_type='text/json')

def mapa_linija(request, pk):
    linija = Linija.objects.get(pk=pk)
    stanice = linija.stanice.all()
    data = serializers.serialize('json', stanice)
    return HttpResponse(data, content_type='text/json')
from django.shortcuts import render
from django.core import serializers
from app.models import Stanica, Linija
from django.http import HttpResponse
import json

def mapa(request):    
    return render(request, 'mapa/index.html')

def mapa_stanice(request):
     stanice = Stanica.objects.all()
     data = serializers.serialize('json',stanice)
     return HttpResponse(data, content_type='text/json')
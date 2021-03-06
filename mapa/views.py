from django.shortcuts import render
from django.core import serializers
from app.models import Stanica, Linija
from django.http import HttpResponse
import json

def mapa(request):
 #   stanice =  Stanica.objects.all()
#    data = [{'naziv': stanica.naziv, 'opis':stanica.opis, 'tacka':stanica.tacka} for stanica in stanice]
    
   # data = serializers.serialize('json', data)
   ## rez = json.dumps(data)
    
    return render(request, 'mapa/index.html')
 #   return HttpResponse(rez, content_type='text/json')

def mapa_stanice(request):
     stanice = Stanica.objects.all()
     data = serializers.serialize('json',stanice)
     print(data)

     return HttpResponse(data, content_type='text/json')
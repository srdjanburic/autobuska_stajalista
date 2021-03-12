from django.shortcuts import render
from app.models import Stanica, Linija
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
import json

# Create your views here.
def mapa_stanice(request):
     stanice = Stanica.objects.all()
     data = serializers.serialize('json',stanice)
     return HttpResponse(data, content_type='text/json')

def mapa_linija(request, pk):
    linija = Linija.objects.get(pk=pk)
    stanice = linija.stanice.all()
    data = serializers.serialize('json', stanice)
    return HttpResponse(data, content_type='text/json')


from django.shortcuts import render, redirect
from django.core import serializers
from app.models import Stanica, Linija
from django.http import HttpResponse
import json
from app.forms import StanicaModelForm
from app.models import Stanica


def mapa(request):    
    if request.method == 'GET':
        form = StanicaModelForm()
        return render(request, 'mapa/index.html', {"form":form})
    elif request.method == 'POST':
        form = StanicaModelForm(request.POST)
        if form.is_valid():
            n= form.cleaned_data['naziv']
            o = form.cleaned_data['opis']
            t = form.cleaned_data['tacka']
            Stanica(naziv=n, opis=o, tacka=t).save()
            return redirect('mapa:prikaz_stanica')
        

        



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
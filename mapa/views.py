from django.shortcuts import render, redirect

from app.models import Stanica, Linija
from django.http import HttpResponse

from app.forms import StanicaModelForm



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

def mapa_dodaj_liniju(request):
   
    return render(request, 'mapa/dodaj_liniju.html')
    
        
    





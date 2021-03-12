from django.shortcuts import render, redirect, reverse

from app.models import Stanica, Linija
from django.http import HttpResponse
from django.views.generic import CreateView
from app.forms import StanicaModelForm, LinijaModelForm
from .forms import  DodajLinijuForm

class StaniceView(CreateView):
    template_name = 'mapa/index.html'
    form_class = StanicaModelForm
    def get_success_url(self):
        return reverse('mapa:prikaz_stanica')

def mapa_linija_prikaz(request, pk):
    linija = Linija.objects.get(pk=pk)    
    return render(request, 'mapa/linija.html', {'linija':linija, 'pk':pk})


class DodajLinijuView(CreateView):   
    template_name = 'mapa/dodaj_liniju.html'
    form_class = LinijaModelForm            
    
def mapa_linija_dodaj(request):
    if request.method == 'GET':
        form = DodajLinijuForm()
        return render(request, 'mapa/dodaj_liniju.html', {'form':form})
    elif request.method == 'POST':
        form = DodajLinijuForm(request.POST)
        if form.is_valid():
            naziv = form.cleaned_data['naziv']
            lista_stanica = [int(i) for i in list(form.cleaned_data['stanice'].split(','))]
            
            stanice = Stanica.objects.filter(pk__in=lista_stanica)
            
            linija = Linija.objects.create(naziv=naziv)
            for stanica in stanice.iterator():
                linija.stanice.add(stanica)
            return mapa_linija_prikaz(request,linija.pk)
            
            






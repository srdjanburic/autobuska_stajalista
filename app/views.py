from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .forms import LinijaModelForm, StanicaModelForm


from .models import Stanica, Linija

class PocetnaView(generic.TemplateView):
    template_name = 'app/pocetna.html'

class DodajStanicuView(generic.CreateView):
    template_name = 'app/dodaj_stanicu.html'
    form_class = StanicaModelForm    

class StaniceView(generic.ListView):
    template_name = 'app/stanice.html'
    model = Stanica
    context_object_name = 'lista_stanica'

class DodajLinijuView(generic.CreateView):
    template_name = 'app/dodaj_liniju.html'    
    form_class = LinijaModelForm

class LinijeView(generic.ListView):
    template_name = 'app/linije.html'
    model = Linija
    context_object_name = 'lista_linija'
   

    


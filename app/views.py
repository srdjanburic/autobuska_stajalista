from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Stanica
# Create your views here.

class DodajStanicuView(generic.CreateView):
    template_name = 'app/dodaj_stanicu.html'
    model = Stanica
    fields = '__all__'

class StaniceView(generic.ListView):
    template_name = 'app/stanice.html'
    model = Stanica
    context_object_name = 'lista_stanica'

    


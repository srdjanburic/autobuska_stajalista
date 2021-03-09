
from django.urls import path
from . import views

app_name = 'mapa'

urlpatterns = [
    path('', views.mapa, name='prikaz_stanica'),
    path('linija/<int:pk>', views.mapa_linija_prikaz, name='prikaz_linije'),
   
    
]
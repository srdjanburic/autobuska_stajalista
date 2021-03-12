
from django.urls import path
from . import views

app_name = 'mapa'

urlpatterns = [
    path('', views.StaniceView.as_view(), name='prikaz_stanica'),
    path('linija/<int:pk>', views.mapa_linija_prikaz, name='prikaz_linije'),
    path('linija/dodaj', views.mapa_linija_dodaj, name='dodaj_liniju')
   
    
]
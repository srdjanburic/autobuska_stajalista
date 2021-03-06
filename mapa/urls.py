
from django.urls import path
from . import views

app_name = 'mapa'

urlpatterns = [
    path('', views.mapa, name='mapa'),
    path('api/stanice', views.mapa_stanice, name='stanice')
]
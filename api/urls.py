from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
     path('stanice', views.mapa_stanice, name='stanice'),
     path('linija/<int:pk>', views.mapa_linija, name='linija'),

]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.DodajStanicuView.as_view(), name = 'dodaj_stanicu'),
    path('stanice', views.StaniceView.as_view(), name = 'stanice')
]
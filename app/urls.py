from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('dodaj_stanicu', views.DodajStanicuView.as_view(), name = 'dodaj_stanicu'),
    path('stanice', views.StaniceView.as_view(), name = 'stanice'),
    path('dodaj_liniju', views.DodajLinijuView.as_view(), name='dodaj_liniju'),
    path('linije', views.LinijeView.as_view(), name='linije')
]
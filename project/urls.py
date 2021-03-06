
from django.contrib import admin
from django.urls import path, include
from app.views import PocetnaView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('app.urls', namespace='app')),
    path('', PocetnaView.as_view(), name='pocetna'),
    path('mapa/', include('mapa.urls', namespace='mapa')),

    
]

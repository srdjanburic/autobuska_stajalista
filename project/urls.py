
from django.contrib import admin
from django.urls import path, include
from app.views import PocetnaView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('app.urls')),
    path('', PocetnaView.as_view(), name='pocetna')
    
]

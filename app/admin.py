from django.contrib import admin

# Register your models here.
from .models import Stanica, Linija

admin.site.register(Stanica)
admin.site.register(Linija)
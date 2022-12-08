from django.contrib import admin

# Register your models here.
from .models import Directores, Películas, Buscador

admin.site.register(Directores)
admin.site.register(Películas)
admin.site.register(Buscador)
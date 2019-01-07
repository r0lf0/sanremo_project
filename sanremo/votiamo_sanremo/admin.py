from django.contrib import admin

from .models import Concorrente, Categoria, Voto

admin.site.register(Concorrente)
admin.site.register(Categoria)
admin.site.register(Voto)

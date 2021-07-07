from django.contrib import admin
from .models import Componente, Marca, Producto, Contacto
# Register your models here.
admin.site.register(Marca)
admin.site.register(Producto)
admin.site.register(Contacto)
admin.site.register(Componente)
from django.contrib import admin
from .models import Componente, Cotizar, Marca, Producto, Contacto, Usuario
# Register your models here.
admin.site.register(Marca)
admin.site.register(Producto)
admin.site.register(Contacto)
admin.site.register(Componente)
admin.site.register(Usuario)
admin.site.register(Cotizar)
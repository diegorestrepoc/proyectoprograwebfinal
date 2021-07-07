from django.contrib import admin
from .models import Marca, Producto, Contacto
# Register your models here.
admin.site.register(Marca)
admin.site.register(Producto)
admin.site.register(Contacto)
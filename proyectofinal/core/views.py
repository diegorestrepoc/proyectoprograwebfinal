from django.utils import html
from .models import Componente, Producto, Contacto, Usuario
from django.shortcuts import render , HttpResponse
from .forms import ContactoForm, UsuarioForm, CotizacionForm, ProductoForm
from rest_framework import viewsets
from .serializers import ProductoSerializer

class ProductoViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

def index(request):
    productos = Producto.objects.all()
    

    return render(request,"core/index.html",{'productos':productos})

def conocenos(request):
    return render(request,"core/conocenos.html")

def contact(request):

    data = {
        'form': ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Mensaje enviado"
        else:
            data["form"] = formulario
    return render(request,"core/contact.html", data)

def cotizacion(request):
    data = {
        'form': CotizacionForm()
    }
    if request.method == 'POST':
        formulario = CotizacionForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Cotizacion registrada"
        else:
            data["form"] = formulario
    
    return render(request,"core/cotizacion.html", data)
    

def iniciosesion(request):
    return render(request,"core/iniciosesion.html")

def registro(request):
    data = {
        'form': UsuarioForm()
    }
    if request.method == 'POST':
        formulario = UsuarioForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Usuario registrado"
        else:
            data["form"] = formulario
    
    return render(request,"core/registro.html", data)

def add_producto(request):

    data = {
        'form': ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Producto agregado"
        else:
            data["form"] = formulario
    return render(request,"core/add_producto.html", data)

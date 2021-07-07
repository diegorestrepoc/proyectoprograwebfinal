from .models import Producto, Contacto
from django.shortcuts import render , HttpResponse
from .forms import ContactoForm

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
    return render(request,"core/cotizacion.html")

def iniciosesion(request):
    return render(request,"core/iniciosesion.html")

def registro(request):
    return render(request,"core/registro.html")



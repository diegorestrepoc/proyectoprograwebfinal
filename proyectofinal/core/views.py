from django.http import Http404
from django.utils import html
from .models import Componente, Producto, Contacto, Usuario
from django.shortcuts import render , HttpResponse, redirect, get_object_or_404
from .forms import ContactoForm, UsuarioForm, CotizacionForm, ProductoForm
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import ProductoSerializer
from django.core.paginator import Paginator
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated



@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated),)
def lista_producto(request):
    """
    Lista todos los vehiculos
    """
    if request.method == 'GET':
        producto = Producto.objects.all()
        serializer = ProductoSerializer(producto, many=True)
        return Response(serialize.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=statu.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductoViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

def index(request):
    productos = Producto.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(productos, 5)
        productos = paginator.page(page)
    except:
        raise Http404
    data= {
         'entity': productos,
         'paginator': paginator
    }

    return render(request,"core/index.html", data)

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


def modificarproducto(request,idProducto):
    producto = get_object_or_404(Producto, idProducto=idProducto)

    data = {
        'form': ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listarproducto")
        data["form"] = formulario

    return render(request, 'core/modificarproducto.html', data)

def eliminarproducto(request, idProducto):
    producto = get_object_or_404(Producto, idProducto=idProducto)
    producto.delete()
    return redirect(to="listarproductos")



def listarproductos(request):
    productos = Producto.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(productos, 5)
        productos = paginator.page(page)
    except:
        raise Http404
    data= {
         'entity': productos,
         'paginator': paginator
    }

    return render(request,'core/listarproducto.html', data)
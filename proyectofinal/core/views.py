from django.shortcuts import render , HttpResponse

def index(request):
    return render(request,"core/index.html")

def conocenos(request):
    return render(request,"core/conocenos.html")

def contact(request):
    return render(request,"core/contact.html")

def cotizacion(request):
    return render(request,"core/cotizacion.html")

def iniciosesion(request):
    return render(request,"core/iniciosesion.html/")

def registro(request):
    return render(request,"core/registro.html")



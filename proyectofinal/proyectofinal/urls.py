"""proyectofinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""



from django.contrib import admin
from django.urls import path, include
from core import views
from core.views import ProductoViewset, lista_producto
from django.conf import settings
from rest_framework import routers


router = routers.DefaultRouter()
router.register('producto', ProductoViewset)

urlpatterns = [
    path('',views.index, name='index'),
    path('conocenos/',views.conocenos, name='conocenos'),
    path('contact/',views.contact, name='contact'),
    path('cotizacion/',views.cotizacion, name='cotizacion'),
    path('iniciosesion/',views.iniciosesion, name='iniciosesion'),
    path('registro/',views.registro, name='registro'),
    path('agregarproducto/',views.add_producto, name='agregar_producto'),
    path('listarproducto/',views.listarproductos, name='listar_producto'),
    path('modificarproducto/<idProducto>/',views.modificarproducto, name='modificar_producto'),
    path('eliminarproducto/<idProducto>/', views.eliminarproducto, name='eliminar_producto'),
    path('lista_productos', lista_producto, name="lista_productos"),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
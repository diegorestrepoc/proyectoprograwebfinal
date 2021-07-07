from django.db import models

# Create your models here.
class Marca(models.Model):
    idMarca = models.IntegerField(primary_key=True, verbose_name='Id')
    nombreMarca = models.CharField(max_length=50, verbose_name="Marca")

    class Meta:
        verbose_name = 'marca'
        verbose_name_plural = 'marcas'
        ordering = ["nombreMarca"]

    def __str__(self):
        return self.nombreMarca

class Producto(models.Model):
    idProducto = models.CharField(primary_key=True, max_length=10,verbose_name='Código')
    descripcion = models.CharField(max_length=100,verbose_name='Descripción')
    precio = models.IntegerField(verbose_name='Precio Unitario')
    cantidad = models.IntegerField(verbose_name='Stock')
    imagen = models.ImageField(verbose_name='Imagen',upload_to='productos',null=True,blank=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    class Meta:
            verbose_name = 'producto'
            verbose_name_plural = 'productos'
            ordering = ["descripcion"]

    def __str__(self):
            return self.descripcion   

class Contacto(models.Model):
    asunto = models.CharField(max_length=50,verbose_name='Asunto')
    email = models.CharField(max_length=40,verbose_name='Correo')
    mensaje = models.TextField(max_length=200, verbose_name='Mensaje')
    
    created = models.DateTimeField(verbose_name='Fecha creación',auto_now_add=True)

    class Meta:
        verbose_name = 'contacto'
        verbose_name_plural = 'contactos'
        ordering = ["-created"]

    def __str__(self):
        return self.asunto
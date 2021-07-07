from django.db import models

# Create your models here.
class Marca(models.Model):
    idMarca = models.CharField(primary_key=True,max_length=50, verbose_name='Id')
    nombreMarca = models.CharField(max_length=50, verbose_name="Marca")

    class Meta:
        verbose_name = 'marca'
        verbose_name_plural = 'marcas'
        ordering = ["nombreMarca"]

    def __str__(self):
        return self.nombreMarca

class Componente(models.Model):
    idComponente = models.CharField(primary_key=True, max_length=50, verbose_name='Id')
    nombreComponente = models.CharField(max_length=50, verbose_name="Componente")

    class Meta:
        verbose_name = 'componente'
        verbose_name_plural = 'componentes'
        ordering = ["nombreComponente"]

    def __str__(self):
        return self.nombreComponente

class Producto(models.Model):
    idProducto = models.CharField(primary_key=True, max_length=10,verbose_name='Código')
    descripcion = models.CharField(max_length=100,verbose_name='Descripción')
    precio = models.IntegerField(verbose_name='Precio Unitario')
    cantidad = models.IntegerField(verbose_name='Stock')
    imagen = models.ImageField(verbose_name='Imagen',upload_to='productos',null=True,blank=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    componente = models.ForeignKey(Componente, on_delete=models.CASCADE)

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


opciones_genero = [
    [0,"masculino"],
    [1,"femenino"],
    [2,"no binario"]
]

opciones_comuna = [
    [0,"santiago"],
    [1,"san joaquin"],
    [2,"macul"],
    [3,"quinta normal"],
    [4,"cerro navia"],
    [5,"ñuñoa"],
    [6,"renca"],
    [7,"las condes"]
]
class Usuario(models.Model):
    usuario = models.CharField(max_length=20,verbose_name='Usuario')
    rut = models.CharField(max_length=12,verbose_name='Rut')
    nombre = models.CharField(max_length=50,verbose_name='Nombre')
    email = models.EmailField(max_length=50,verbose_name='Correo')
    genero = models.IntegerField(choices=opciones_genero)
    comuna = models.IntegerField(choices=opciones_comuna)

    class Meta:
        verbose_name= 'usuario'
        verbose_name_plural= 'usuarios'
        ordering=["usuario"]
    def __str__(self):
        return self.usuario


opciones_placa = [
    [0,"MSI H310M PRO-VDH PLUS"],
    [1,"ASUS PRIME B460M-A"],
    [2,"MSI A320M-A PRO MAX"]
]
opciones_procesador = [
    [0,"I5-10400F"],
    [1,"RYZEN 3 3200G"],
    [2,"I3-9100"]
]
opciones_gpu = [
    [0,"GTX 1650 TI"],
    [1,"GTX 3060"],
    [2,"RX 580"]
]
opciones_ram = [
    [0,"CRUCIAL 4GB"],
    [1,"HYPERX 4GB"],
    [2,"A-DATA 8GB"]
]
opciones_fuente = [
    [0,"GIGABYTE 550W"],
    [1,"CORSAIR 450W"],
    [2,"GAMEMAX 650W"]
]
opciones_disco = [
    [0,"WD 500GB"],
    [1,"SEAGATE 2TB"],
    [2,"WD 4TB"]
]
opciones_gabinete = [
    [0,"GEAR BLACKSTAR"],
    [1,"DINON MODEL"],
    [2,"POWER TRAIN LASER FIVE G1"]
]









class Cotizar(models.Model):
    nombre = models.CharField(max_length=20, verbose_name='Nombre')
    placa_madre = models.IntegerField(choices=opciones_placa)
    procesador = models.IntegerField(choices=opciones_procesador)
    gpu = models.IntegerField(choices=opciones_gpu)
    ram = models.IntegerField(choices=opciones_ram)
    fuente = models.IntegerField(choices=opciones_fuente)
    discoduro = models.IntegerField(choices=opciones_disco)
    gabinete = models.IntegerField(choices=opciones_gabinete)
    created = models.DateTimeField(verbose_name='Fecha creación',auto_now_add=True)

    class Meta:
        verbose_name='Cotización'
        verbose_name_plural = 'Cotizaciones'
        ordering=["-created"]
    def __str__(self):
        return self.nombre

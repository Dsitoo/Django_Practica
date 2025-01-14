from django.db import models
import os

# Create your models here.
class Usuario(models.Model): 
    id = models.AutoField(primary_key=True) 
    correo = models.EmailField(max_length=100, unique=True, default='correo@gmail.com') 
    contraseña = models.CharField(max_length=200, default='123456789') 
    username = models.CharField(max_length=50, unique=True, default='username') 
    ADMIN = 1 
    USUARIO = 2 
    ROL_CHOICES = ( (ADMIN, 'Admin'), (USUARIO, 'Usuario'), ) 
    rol = models.IntegerField(choices=ROL_CHOICES, default=USUARIO)
    fotoperfil = models.ImageField(upload_to='img/Img_Usuarios', default='img/default.png')

    def __str__(self): 
        return self.username
    
class Producto(models.Model): 
    id_producto = models.AutoField(primary_key=True) 
    nombre = models.CharField(max_length=100, default='Producto') 
    descripcion = models.CharField(max_length=400 ,default='Descripcion') 
    precio = models.DecimalField(max_digits=20, decimal_places=2, default=0.00) 
    cantidad = models.IntegerField(default=0)
    imagen1 = models.ImageField(upload_to='uploads/', blank=True, null=True, default='media/uploads/default_P.png')
    imagen2 = models.ImageField(upload_to='uploads/', default='media/uploads/default_P.png')
    imagen3 = models.ImageField(upload_to='uploads/', default='media/uploads/default_P.png')
    imagen4 = models.ImageField(upload_to='uploads/', default='media/uploads/default_P.png')
    imagen5 = models.ImageField(upload_to='uploads/', default='media/uploads/default_P.png')
    especificaciones = models.CharField(max_length=300 ,default='Especificaciones')
    
    def __str__(self):
        return self.nombre
    
    def delete(self, *args, **kwargs):
        # Nombre de la imagen por defecto
        default_image_name = 'default_P.png'
        
        # Lista de imágenes
        imagenes = [self.imagen1, self.imagen2, self.imagen3, self.imagen4, self.imagen5]

        # Iterar sobre las imágenes
        for imagen in imagenes:
            if imagen:
                # Obtener solo el nombre del archivo (sin la ruta completa)
                imagen_name = os.path.basename(imagen.path)

                # Verificar si la imagen no es la imagen por defecto
                if imagen_name != default_image_name and os.path.isfile(imagen.path):
                    os.remove(imagen.path)

        # Llamar al método `delete` de la clase base
        super().delete(*args, **kwargs)
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuario, Producto
from .forms import Login, Register, Product
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'login_register.html',{
        'form_L': Login(), 'form_R': Register()
    })
    else:
        Usuario.objects.get(correo=request.POST['correo'], contraseña=request.POST['contraseña'])
        return redirect('catalogo')

def cerrar_se(request):
    logout(request)
    messages.success(request, '¡Has cerrado sesión exitosamente!')
    return redirect('index')

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html',{
        'form_R': Register()
    })
    else:
        Usuario.objects.create(username=request.POST['username'], correo=request.POST['correo'], contraseña=request.POST['contraseña'])
        return redirect('login')

def catalogo(request):
    productos = Producto.objects.all()
    return render(request, 'catalogo.html', {
        'productos': productos
    })

from django.core.files.storage import default_storage
from django.conf import settings

def aggproducto(request):
    if request.method == 'GET':
        return render(request, 'admin/aggproductos.html', {
            'form_P': Product()
        })
    else:
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        cantidad = request.POST.get('cantidad')
        especificaciones = request.POST.get('especificaciones')
        
        imagen1 = request.FILES.get('imagen1')
        imagen2 = request.FILES.get('imagen2')
        imagen3 = request.FILES.get('imagen3')
        imagen4 = request.FILES.get('imagen4')
        imagen5 = request.FILES.get('imagen5')

        default_image_path = 'uploads/default_P.png'
        
        if not imagen1:
            imagen1 = default_storage.open(default_image_path).name
        if not imagen2:
            imagen2 = default_storage.open(default_image_path).name
        if not imagen3:
            imagen3 = default_storage.open(default_image_path).name
        if not imagen4:
            imagen4 = default_storage.open(default_image_path).name
        if not imagen5:
            imagen5 = default_storage.open(default_image_path).name

        producto = Producto(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            cantidad=cantidad,
            especificaciones=especificaciones,
            imagen1=imagen1,
            imagen2=imagen2,
            imagen3=imagen3,
            imagen4=imagen4,
            imagen5=imagen5,
        )

        producto.save()

        return redirect('catalogo')

def detalle_producto(request, id_producto):
    producto = get_object_or_404(Producto, pk=id_producto)
    return render(request, 'productos.html', {'producto': producto})

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'admin/lista_productos.html', {'productos': productos})

def editar_producto(request, producto_id):
    # Obtener el producto por id
    producto = get_object_or_404(Producto, id_producto=producto_id)

    if request.method == 'POST':
        # Crear una instancia del formulario con los datos del producto
        form = Product(request.POST, request.FILES, instance=producto)
        
        if form.is_valid():
            form.save()  # Guardamos los cambios
            return redirect('catalogo')  # Redirigir a la vista de productos (ajusta la URL a tu necesidad)
    else:
        # Mostrar el formulario con los datos actuales del producto
        form = Product(instance=producto)

    return render(request, 'admin/editar_producto.html', {'form': form, 'producto': producto})

def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id_producto=producto_id)

    # Eliminar el producto
    producto.delete()

    # Redirigir a la lista de productos después de eliminar
    return redirect('catalogo')  # Cambia 'catalogo' por la vista que te gustaría mostrar después de eliminar

from ftplib import MAXLINE
from django import forms
from .models import Producto

class Login(forms.Form):
    correo = forms.CharField(label='Correo', max_length=200, widget=forms.EmailInput(attrs={'placeholder': 'Ingrese su correo', 'class' : 'inputL'}))
    contraseña = forms.CharField(label='Contraseña', max_length=200, widget=forms.PasswordInput(attrs={'placeholder': 'Ingrese su contraseña', 'class' : 'inputL'}))

class Register(forms.Form):
    username = forms.CharField(label='Nombre', max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Ingrese su nombre', 'class' : 'inputR'}))
    correo = forms.CharField(label='Correo', max_length=200, widget=forms.EmailInput(attrs={'placeholder': 'Ingrese su correo', 'class' : 'inputR'}))
    contraseña = forms.CharField(label='Contraseña', max_length=200, widget=forms.PasswordInput(attrs={'placeholder': 'Ingrese su contraseña', 'class' : 'inputR'}))
    contraseña2 = forms.CharField(label='Repetir Contraseña', max_length=200, widget=forms.PasswordInput(attrs={'placeholder': 'Ingrese su contraseña', 'class' : 'inputR'}))

class Product(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'cantidad', 'imagen1', 'imagen2', 'imagen3', 'imagen4', 'imagen5', 'especificaciones']
        
        # Aquí puedes personalizar los widgets si es necesario
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Ingrese el nombre', 'class' : 'inputP'}),
            'descripcion': forms.TextInput(attrs={'placeholder': 'Ingrese la descripción', 'class' : 'inputP'}),
            'precio': forms.NumberInput(attrs={'placeholder': 'Ingrese el precio', 'class' : 'inputP'}),
            'cantidad': forms.NumberInput(attrs={'placeholder': 'Ingrese la cantidad', 'class' : 'inputP'}),
            'imagen1': forms.FileInput(attrs={'class' : 'inputP'}),
            'imagen2': forms.FileInput(attrs={'class' : 'inputP'}),
            'imagen3': forms.FileInput(attrs={'class' : 'inputP'}),
            'imagen4': forms.FileInput(attrs={'class' : 'inputP'}),
            'imagen5': forms.FileInput(attrs={'class' : 'inputP'}),
            'especificaciones': forms.TextInput(attrs={'placeholder': 'Ingrese las especificaciones', 'class' : 'inputP'}),
        }

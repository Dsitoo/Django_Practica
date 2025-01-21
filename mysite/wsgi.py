"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import sys

# Añadir la ruta al directorio raíz de tu proyecto Django (Django_Practica)
sys.path.append('/home/DsiDsi/Django_Practica')

# Especificar el módulo de configuración de Django (mysite.settings)
os.environ['DJANGO_SETTINGS_MODULE', 'mysite.settings']

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()



from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('login/' , views.login, name='login'),
    path('logout/', views.cerrar_se, name='cerrar_se'),
    path('register/', views.register, name='register'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('aggproducto/', views.aggproducto, name='aggproducto'),
    path('producto/<int:id_producto>/', views.detalle_producto, name='detalle_producto'),
    path('lista_productos/', views.lista_productos, name='lista_productos'),
    path('producto/editar/<int:producto_id>/', views.editar_producto, name='editar_producto'),
    path('producto/eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
]   

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

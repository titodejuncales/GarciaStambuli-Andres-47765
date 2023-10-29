from django.urls import path
from Usuarios.views import *
from django import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', iniciarSesion, name ="Login"),
    path('registro/', crearUsuario, name ="Registro"),
    path('logout/', LogoutView.as_view(template_name= "Usuarios/logout.html"), name ="Logout"),
    path('editarusuario/', editarUsuario, name="EditarUsuario"),
    path('agregaravatar/', agregarAvatar, name="AgregarAvatar"),
]
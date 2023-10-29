from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from Usuarios.models import Avatar 


class UsuarioRegistro(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label = "Contraseña", widget = forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir contraseña", widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]


class FormEditar(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label = "Contraseña", widget = forms.PasswordInput, required=False)
    password2 = forms.CharField(label = "Repetir contraseña", widget = forms.PasswordInput, required=False)

    class Meta:
        model = User
        fields = [ "email", "first_name", "last_name", "password1", "password2"]


class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields =[ "imagen"]
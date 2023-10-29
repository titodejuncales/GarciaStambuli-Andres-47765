from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from Usuarios.forms import *
from django.contrib.auth.decorators import login_required

def iniciarSesion(request):#Iniciar sesión
    if 'next' in request.session:#Si existe la variable next, luego de iniciar sesión te deriva a la url almacenada en ella
        next_url = request.GET.get('next')
    else:#Si no existe me deriva a la url de inicio
        next_url=''        
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra= form.cleaned_data.get("password")
            user = authenticate(username = usuario, password = contra)

            if user:
                login(request, user)
                if 'next' in request.session:#Elimina la variable next si existía
                    del request.session['next']  
                    return redirect(next_url)
                else:
                    return render(request,"AppTDJ/inicio.html",{"mensaje": f"Bienvenido {user}"})
                       
        else:
            return render(request,"AppTDJ/inicio.html", {"mensaje":"Datos incorrectos"})
        
    else:
        form = AuthenticationForm()
    return render(request,"Usuarios/login.html", {"form": form})

def crearUsuario(request):#Crear un nuevo usuario
    if request.method == "POST":
        form = UsuarioRegistro(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request,"AppTDJ/inicio.html", {"mensaje":f"Se ha creado el usuario {username}"})
    else:
        form = UsuarioRegistro()

    return render(request, "Usuarios/registro.html", {"form":form})

@login_required
def editarUsuario(request):#Editar usuario
    usuario = request.user

    if request.method == "POST":
        form = FormEditar(request.POST)
            
        if form.is_valid():
            info = form.cleaned_data

            usuario.email = info["email"]
            usuario.first_name = info["first_name"]
            usuario.last_name =  info["last_name"]

            nuevo_password = info.get("password1")
            if nuevo_password:
                usuario.set_password(nuevo_password)

            usuario.save()

            return render(request, "AppTDJ/inicio.html", {"mensaje":"Se han modificado sus datos"})
        
    else:
        form = FormEditar(initial ={
            "email": usuario.email,
            "first_name": usuario.first_name,
            "last_name": usuario.last_name, 
        })
    return render(request, "Usuarios/editarPerfil.html", {"form": form, "usuario":usuario})

@login_required
def agregarAvatar(request): #Agregar avatar
    if request.method =="POST":
        form = AvatarForm(request.POST, request.FILES)

        if form.is_valid():
            usuarioActual = User.objects.get(username=request.user)

            avatar = Avatar(usuario=usuarioActual, imagen=form.cleaned_data["imagen"] )
            avatar.save()

            return render(request, "AppTDJ/inicio.html", {"mensaje":"Se ha agregado tu ávatar"})
        
    else:
        form = AvatarForm()

    return render(request, "Usuarios/agregarAvatar.html", {"form":form})
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from AppTDJ.models import *
from AppTDJ.forms import *


#-----------------------------------------------------------------------------------------------------------------------VARIOS
def inicio(request):
    return render(request, 'AppTDJ/inicio.html')

def sobremi(request):
    return render(request, 'AppTDJ/sobremi.html')

def contacto(request):
    return render(request, 'AppTDJ/contacto.html')

#-----------------------------------------------------------------------------------------------------------------------MONEDAS
class ListaMoneda(ListView):#Ver listado de monedas
    model = Moneda
    template_name = "AppTDJ/Monedalista.html"

class DetalleMoneda(DetailView):#Ver detalle de moneda
    model = Moneda
    template_name = "AppTDJ/Monedadetalle.html"

class CrearMoneda(LoginRequiredMixin, CreateView):#Crear monedas
    login_url = "/AppTDJ/login"
    model = Moneda
    success_url = "/AppTDJ/monedas/lista"
    fields = ["pais", "continente", "valor", "year", "material", "forma", "descripcion", "imgfrente", "imgdorso"]
    template_name = "AppTDJ/Monedaformulario.html"
    
    def handle_no_permission(self):#Almacena el url en la variable next, para luego de iniciar sesión ser redirigido
        self.request.session['next'] = self.request.get_full_path()
        return super().handle_no_permission()
    
    def form_valid(self, form):#Asigna el usuario logueado al campo usuario de la moneda
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class ActualizarMoneda(UserPassesTestMixin, UpdateView):#Actualizar monedas
    login_url = "/AppTDJ/login"
    model = Moneda
    success_url = "/AppTDJ/monedas/lista"
    fields = ["pais", "continente", "valor", "year", "material", "forma", "descripcion","imgfrente", "imgdorso"]
    template_name = "AppTDJ/Monedaformulario.html"
    
    def test_func(self):#Verifica si el usuario está logueado y es el creador de la moneda
        obj = self.get_object()
        return self.request.user.is_authenticated and obj.usuario == self.request.user
    
    def handle_no_permission(self):
        if not self.request.user.is_authenticated:#Verifica si el usuario no está logueado y deriva a iniciar sesión
            self.request.session['next'] = self.request.get_full_path()
            return super().handle_no_permission()
        else:#En caso de que esté logueado pero no sea el usuario creador, arroja un mensaje de error
            return render(self.request, 'AppTDJ/Inicio.html',{"mensaje":"No puedes modificar esta moneda porque no es tuya"})
        

class EliminarMoneda(UserPassesTestMixin, DeleteView):#Eliminar monedas
    login_url = "/AppTDJ/login"
    model = Moneda
    success_url = "/AppTDJ/monedas/lista"
    template_name = "AppTDJ/Monedaeliminar.html"

    def test_func(self):#Verifica si el usuario está logueado y es el creador de la moneda
        obj = self.get_object()
        return self.request.user.is_authenticated and obj.usuario == self.request.user
    
    def handle_no_permission(self):
        if not self.request.user.is_authenticated:#Verifica si el usuario no está logueado y deriva a iniciar sesión
            self.request.session['next'] = self.request.get_full_path()
            return super().handle_no_permission()
        else:#En caso de que esté logueado pero no sea el usuario creador, arroja un mensaje de error
            return render(self.request, 'AppTDJ/Inicio.html',{"mensaje":"No puedes eliminar esta moneda porque no es tuya"})    


def buscarMoneda(request): #Buscar monedas
    return render(request, 'AppTDJ/Monedabuscar.html')

def resultadoMoneda(request):#Resultado de búsqueda de moneda
    if  request.GET["pais"]:
        moneda = request.GET["pais"]
        monedas = Moneda.objects.filter(pais__icontains=moneda)
        return render(request, "AppTDJ/Monedaresultado.html", {"monedas":monedas, "moneda":moneda})
    else:
        return render(request, "AppTDJ/Monedabuscar.html")

@login_required
def milistaMoneda(request): #Ver las monedas creadas por el usuario logueado
    monedas = Moneda.objects.filter(usuario=request.user)
    return render(request, 'AppTDJ/Monedamilista.html', {"monedas":monedas})
  

#-----------------------------------------------------------------------------------------------------------------------BILLETES
class ListaBillete(ListView):#Ver listado de billetes
    model = Billete
    template_name = "AppTDJ/Billetelista.html"

class DetalleBillete(DetailView):#Ver detalle de billete
    model = Billete
    template_name = "AppTDJ/Billetedetalle.html"

class CrearBillete(LoginRequiredMixin, CreateView):#Crear billetes
    login_url = "/AppTDJ/login"
    model = Billete
    success_url = "/AppTDJ/billetes/lista"
    fields = ["pais", "continente", "valor", "year", "material", "descripcion", "imgfrente", "imgdorso"]
    template_name = "AppTDJ/Billeteformulario.html"

    def handle_no_permission(self):#Almacena el url en la variable next, para luego de iniciar sesión ser redirigido
        self.request.session['next'] = self.request.get_full_path()
        return super().handle_no_permission()
    
    def form_valid(self, form):#Asigna el usuario logueado al campo usuario del billete
        form.instance.usuario = self.request.user
        return super().form_valid(form)
    
class ActualizarBillete(UserPassesTestMixin, UpdateView):#Actualizar billete
    login_url = "/AppTDJ/login"
    model = Billete
    success_url = "/AppTDJ/billetes/lista"
    fields = ["pais", "continente", "valor", "year", "material", "descripcion",  "imgfrente", "imgdorso"]
    template_name = "AppTDJ/Billeteformulario.html"

    def test_func(self):#Verifica si el usuario está logueado y es el creador del billete
        obj = self.get_object()
        return self.request.user.is_authenticated and obj.usuario == self.request.user
    
    def handle_no_permission(self):
        if not self.request.user.is_authenticated:#Verifica si el usuario no está logueado y deriva a iniciar sesión
            self.request.session['next'] = self.request.get_full_path()
            return super().handle_no_permission()
        else:#En caso de que esté logueado pero no sea el usuario creador, arroja un mensaje de error
            return render(self.request, 'AppTDJ/Inicio.html',{"mensaje":"No puedes modificar este billete porque no es tuyo"})

class EliminarBillete(UserPassesTestMixin, DeleteView):#Eliminar billete
    login_url = "/AppTDJ/login"
    model = Billete
    success_url = "/AppTDJ/billetes/lista"
    template_name = "AppTDJ/Billeteeliminar.html"

    def test_func(self):#Verifica si el usuario está logueado y es el creador del billete
        obj = self.get_object()
        return self.request.user.is_authenticated and obj.usuario == self.request.user
    
    def handle_no_permission(self):
        if not self.request.user.is_authenticated:#Verifica si el usuario no está logueado y deriva a iniciar sesión
            self.request.session['next'] = self.request.get_full_path()
            return super().handle_no_permission()
        else:#En caso de que esté logueado pero no sea el usuario creador, arroja un mensaje de error
            return render(self.request, 'AppTDJ/Inicio.html',{"mensaje":"No puedes eliminar este billete porque no es tuyo"})


def buscarBillete(request):#Buscar billetes
    return render(request, 'AppTDJ/Billetebuscar.html')

def resultadoBillete(request):#Resultado de búsqueda de billetes
    if request.GET["pais"]:
        billete = request.GET["pais"]
        billetes = Billete.objects.filter(pais__icontains=billete)

        return render(request, "AppTDJ/Billeteresultado.html", {"billetes":billetes, "billete":billete})

    else:
        return render(request, "AppTDJ/Billetebuscar.html")
    
@login_required
def milistaBillete(request):#Ver los billetes creados por el usuario logueado
   billetes = Billete.objects.filter(usuario=request.user)
   return render(request, 'AppTDJ/Billetemilista.html', {"billetes":billetes})


#-----------------------------------------------------------------------------------------------------------------------ESTAMPILLAS
class ListaEstampilla(ListView):#Ver listado de estampillas
    model = Estampilla
    template_name = "AppTDJ/Estampillalista.html"

class DetalleEstampilla(DetailView):#Ver detalle de estampilla
    model = Estampilla
    template_name = "AppTDJ/Estampilladetalle.html"

class CrearEstampilla(LoginRequiredMixin, CreateView):#Crear estampillas
    login_url = "/AppTDJ/login"
    model = Estampilla
    success_url = "/AppTDJ/estampillas/lista"
    fields = ["pais", "valor", "year", "descripcion", "forma",  "imgfrente"]
    template_name = "AppTDJ/Estampillaformulario.html"
    
    def handle_no_permission(self):#Almacena el url en la variable next, para luego de iniciar sesión ser redirigido
        self.request.session['next'] = self.request.get_full_path()
        return super().handle_no_permission()
    
    def form_valid(self, form):#Asigna el usuario logueado al campo usuario de la estampilla
        form.instance.usuario = self.request.user
        return super().form_valid(form)
    
class ActualizarEstampilla(UserPassesTestMixin, UpdateView):#Actualizar estampilla
    login_url = "/AppTDJ/login"
    model = Estampilla
    success_url = "/AppTDJ/estampillas/lista"
    fields = ["pais", "valor", "year", "descripcion", "forma", "imgfrente"]
    template_name = "AppTDJ/Estampillaformulario.html"

    def test_func(self):#Verifica si el usuario está logueado y es el creador de la estampilla
        obj = self.get_object()
        return self.request.user.is_authenticated and obj.usuario == self.request.user
    
    def handle_no_permission(self):
        if not self.request.user.is_authenticated:#Verifica si el usuario no está logueado y deriva a iniciar sesión
            self.request.session['next'] = self.request.get_full_path()
            return super().handle_no_permission()
        else:#En caso de que esté logueado pero no sea el usuario creador, arroja un mensaje de error
            return render(self.request, 'AppTDJ/Inicio.html',{"mensaje":"No puedes modificar esta estampilla porque no es tuya"})

class EliminarEstampilla(UserPassesTestMixin, DeleteView):#Eliminar estampilla
    login_url = "/AppTDJ/login"
    model = Estampilla
    success_url = "/AppTDJ/estampillas/lista"
    template_name = "AppTDJ/Estampillaeliminar.html"

    def test_func(self):#Verifica si el usuario está logueado y es el creador de la estampilla
        obj = self.get_object()
        return self.request.user.is_authenticated and obj.usuario == self.request.user
    
    def handle_no_permission(self):
        if not self.request.user.is_authenticated:#Verifica si el usuario no está logueado y deriva a iniciar sesión
            self.request.session['next'] = self.request.get_full_path()
            return super().handle_no_permission()
        else:#En caso de que esté logueado pero no sea el usuario creador, arroja un mensaje de error
            return render(self.request, 'AppTDJ/Inicio.html',{"mensaje":"No puedes eliminar esta estampilla porque no es tuya"})


def buscarEstampilla(request):#Buscar estampilla
    return render(request, 'AppTDJ/Estampillabuscar.html')

def resultadoEstampilla(request):#Resultado de búsqueda de estampilla
    if request.GET["pais"]:
        estampilla = request.GET["pais"]
        estampillas = Estampilla.objects.filter(pais__icontains = estampilla)

        return render(request, "AppTDJ/Estampillaresultado.html", {"estampillas":estampillas, "estampilla":estampilla})

    else:
        return render(request, "AppTDJ/Estampillabuscar.html")
    
@login_required
def milistaEstampilla(request):#Ver las estampillas creadas por el usuario logueado
   estampillas = Estampilla.objects.filter(usuario=request.user)
   return render(request, 'AppTDJ/Estampillamilista.html', {"estampillas":estampillas})


#-----------------------------------------------------------------------------------------------------------------------FICHAS Y MEDALLAS

class ListaFicha(ListView):#Ver listado de fichas y medallas
    model = FichayMedalla
    template_name = "AppTDJ/Fichalista.html"

class DetalleFicha(DetailView):#Ver detalle de ficha o medalla
    model = FichayMedalla
    template_name = "AppTDJ/Fichadetalle.html"

class CrearFicha(LoginRequiredMixin, CreateView):#Crear fichas y medallas
    login_url = "/AppTDJ/login"
    model = FichayMedalla
    success_url = "/AppTDJ/fichasymedallas/lista"
    fields = ["tipodeobjeto", "pais", "valor", "year", "descripcion", "forma", "imgfrente", "imgdorso"]
    template_name = "AppTDJ/Fichaformulario.html"

    def handle_no_permission(self):#Almacena el url en la variable next, para luego de iniciar sesión ser redirigido
        self.request.session['next'] = self.request.get_full_path()
        return super().handle_no_permission()
    
    def form_valid(self, form):#Asigna el usuario logueado al campo usuario de la ficha o medalla
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class ActualizarFicha(UserPassesTestMixin, UpdateView):#Actualizar ficha o medalla
    login_url = "/AppTDJ/login"
    model = FichayMedalla
    success_url = "/AppTDJ/fichasymedallas/lista"
    fields = ["tipodeobjeto", "pais", "valor", "year", "descripcion", "forma", "imgfrente", "imgdorso"]
    template_name = "AppTDJ/Fichaformulario.html"

    def test_func(self):#Verifica si el usuario está logueado y es el creador de la ficha o medalla
        obj = self.get_object()
        return self.request.user.is_authenticated and obj.usuario == self.request.user
    
    def handle_no_permission(self):
        if not self.request.user.is_authenticated:#Verifica si el usuario no está logueado y deriva a iniciar sesión
            self.request.session['next'] = self.request.get_full_path()
            return super().handle_no_permission()
        else:#En caso de que esté logueado pero no sea el usuario creador, arroja un mensaje de error
            return render(self.request, 'AppTDJ/Inicio.html',{"mensaje":"No puedes modificar este objeto porque no es tuyo"})

class EliminarFicha(UserPassesTestMixin, DeleteView):#Eliminar ficha o medalla
    login_url = "/AppTDJ/login"
    model = FichayMedalla
    success_url = "/AppTDJ/fichasymedallas/lista"
    template_name = "AppTDJ/Fichaeliminar.html"

    def test_func(self):#Verifica si el usuario está logueado y es el creador de la ficha o medalla
        obj = self.get_object()
        return self.request.user.is_authenticated and obj.usuario == self.request.user
    
    def handle_no_permission(self):
        if not self.request.user.is_authenticated:#Verifica si el usuario no está logueado y deriva a iniciar sesión
            self.request.session['next'] = self.request.get_full_path()
            return super().handle_no_permission()
        else:#En caso de que esté logueado pero no sea el usuario creador, arroja un mensaje de error
            return render(self.request, 'AppTDJ/Inicio.html',{"mensaje":"No puedes eliminar este objeto porque no es tuyo"})


def buscarFicha(request):#Buscar fichas y medallas
    return render(request, 'AppTDJ/Fichabuscar.html')

def resultadoFicha(request):#Resultado de búqueda de fichas y medallas
    if request.GET["tipodeobjeto"]:
        ficha = request.GET["tipodeobjeto"]
        fichas = FichayMedalla.objects.filter(tipodeobjeto__icontains=ficha)

        return render(request, "AppTDJ/Ficharesultado.html", {"fichas":fichas, "ficha":ficha})

    else:
        return render(request, "AppTDJ/Fichabuscar.html")
    
@login_required
def milistaFicha(request):#Ver las fichas y medallas creadas por el usuario logueado
   fichas = FichayMedalla.objects.filter(usuario=request.user)
   return render(request, 'AppTDJ/Fichamilista.html', {"fichas":fichas})






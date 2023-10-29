from django.urls import path
from AppTDJ.views import *



urlpatterns = [
    path('', inicio, name ="Inicio"),
    path('sobremi/', sobremi, name ="Sobremi"),
    path('contacto/', contacto, name ="Contacto"),

    #Monedas
    path('monedas/lista/', ListaMoneda.as_view(), name = "monedaLista"),
    path('monedas/<int:pk>', DetalleMoneda.as_view(), name = "monedaDetalle" ),
    path('monedas/crear/', CrearMoneda.as_view(), name = "monedaCrear" ),
    path('monedas/actualizar/<int:pk>', ActualizarMoneda.as_view(), name = "monedaActualizar" ),
    path('monedas/eliminar/<int:pk>', EliminarMoneda.as_view(), name = "monedaEliminar"),
    path('monedas/buscar/', buscarMoneda, name = "monedaBuscar"),
    path('monedas/resultado/', resultadoMoneda, name = "monedaResultado"),
    path('monedas/milista/', milistaMoneda, name = "monedaMilista"),
    
    #Billete
    path('billetes/lista/', ListaBillete.as_view(), name = "billeteLista"),
    path('billetes/<int:pk>', DetalleBillete.as_view(), name = "billeteDetalle" ),
    path('billetes/crear/', CrearBillete.as_view(), name = "billeteCrear" ),
    path('billetes/actualizar/<int:pk>', ActualizarBillete.as_view(), name = "billeteActualizar" ),
    path('billetes/eliminar/<int:pk>', EliminarBillete.as_view(), name = "billeteEliminar"),
    path('billetes/buscar/', buscarBillete, name = "billeteBuscar"),
    path('billetes/resultado/', resultadoBillete, name = "billeteResultado"),
    path('billetes/milista/', milistaBillete, name = "billeteMilista"),

    #Estampilla
    path('estampillas/lista/', ListaEstampilla.as_view(), name ="estampillaLista"),
    path('estampillas/<int:pk>', DetalleEstampilla.as_view(), name ="estampillaDetalle" ),
    path('estampillas/crear/', CrearEstampilla.as_view(), name = "estampillaCrear" ),
    path('estampillas/actualizar/<int:pk>', ActualizarEstampilla.as_view(), name = "estampillaActualizar" ),
    path('estampillas/eliminar/<int:pk>', EliminarEstampilla.as_view(), name = "estampillaEliminar"),
    path('estampillas/buscar/', buscarEstampilla, name = "estampillaBuscar"),
    path('estampillas/resultado/', resultadoEstampilla, name = "estampillaResultado"),
    path('estampillas/milista/', milistaEstampilla, name = "estampillaMilista"),

    #Fichas y medallas
    path('fichasymedallas/lista/', ListaFicha.as_view(), name = "fichaLista"),
    path('fichasymedallas/<int:pk>', DetalleFicha.as_view(), name = "fichaDetalle" ),
    path('fichasymedallas/crear/', CrearFicha.as_view(), name = "fichaCrear" ),
    path('fichasymedallas/actualizar/<int:pk>', ActualizarFicha.as_view(), name = "fichaActualizar" ),
    path('fichasymedallas/eliminar/<int:pk>', EliminarFicha.as_view(), name = "fichaEliminar"),
    path('fichasymedallas/buscar/', buscarFicha, name = "fichaBuscar"),
    path('fichasymedallas/resultado/', resultadoFicha, name = "fichaResultado"),
    path('fichasymedallas/milista/', milistaFicha, name = "fichaMilista"),

]

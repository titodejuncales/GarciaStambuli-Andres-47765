# GarciaStambuli-Andres-47765
# ProyectoTDJ
## Creado por Titodejuncales

## Cómo instalar y ejecutar el proyecto

- Instalar Python
- Instalar Django
- Instalar Pillow
- Ejecutar las migraciones

  $python manage.py makemigrations
  
  $python manage.py migrate
  
- Ejecutar el proyecto

  $python manage.py runserver

## Usuario administrador: titodj
## Contraseña: python123

## Acerca del proyecto
Se trata de una página web para gestionar colecciones.
La página cuenta con cuatro secciones: monedas, billetes, estampillas y fichas y medallas.
En cada una de estas secciones vas a encontrar tres botones para acceder:
- a la creación de nuevos artículos
- a la búsqueda de artículos creados anteriormente
- a la visualización en forma de lista de todos los artículos creados.
Si el usuario se encuentra logueado, se habilita un nuevo botón donde podrá acceder a una lista con todos los artículos creados por ese usuario.
Desde cualquiera de estas vistas se podrá acceder a visualizar el detalle del objeto, actualizar su información o eliminarlo, aunque para actualizar o eliminar un objeto
el usuario debe ser el creador del mismo.
Para crear un nuevo artículo sólo se requerirá que el usuario esté logueado.
En caso que se intente acceder a una vista que requiere estar logueado sin haberlo hecho previamente, te derivará a la página de inicio de sesión y luego de completar el inicio
nuevamente te llevará a la página a la cual estabas tratando de acceder.
Si el usuario se encuentra logueado pero intenta modificar un objeto que no es de su propiedad la página mostrará un mensaje notificando la falta de permisos.

Por otro lado, como se mencionó anteriormente, la página cuenta con la posibilidad de crear un usuario para poder gestionar su propia colección, el cual podrá ingresar sus datos
personales, agregar un ávatar, editar su información guardada anteriormente, iniciar y cerrar sesión.

Por último, al pie de página hay dos links con acceso a información personal del creador de la página y a los medios de contacto.

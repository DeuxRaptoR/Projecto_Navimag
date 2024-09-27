"""
URL configuration for Proyecto_Web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from buques import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.mostrarIndex),
    path('login', views.iniciarSesion),
    path('logout', views.cerrarSesion),

    path('menu_principal', views.mostrarMenu),
    path('calendario_admin', views.mostrarMenuCalendario),


    path('form_registrar_buque', views.mostrarFormRegistrarBuque),
    path('registrar_buque', views.registrarBuque),
    path('form_actualizar_buque/<int:id>', views.mostrarFormActualizarBuque),
    path('actualizar_buque/<int:id>', views.actualizarBuque),
    path('eliminar_buque/<int:id>', views.eliminarBuque),

    path('registrar_departamento', views.registrarDepartamento),
    path('form_actualizar_departamento/<int:id>', views.mostrarFormActualizarDepartamento),
    path('actualizar_departamento/<int:id>', views.actualizarDepartamento),
    path('eliminar_departamento/<int:id>', views.eliminarDepartamento),

    path('registrar_sistema', views.registrarSistema),
    path('form_actualizar_sistema/<int:id>', views.mostrarFormActualizarSistema),
    path('actualizar_sistema/<int:id>', views.actualizarSistema),
    path('eliminar_sistema/<int:id>', views.eliminarSistema),

    path('registrar_equipo', views.registrarEquipo),
    path('form_actualizar_equipo/<int:id>', views.mostrarFormActualizarEquipo),
    path('actualizar_equipo/<int:id>', views.actualizarEquipo),
    path('eliminar_equipo/<int:id>', views.eliminarEquipo),

    path('registrar_equipos', views.registrarEquipos),
    path('form_actualizar_equipos/<int:id>', views.mostrarFormActualizarEquipos),
    path('actualizar_equipos/<int:id>', views.actualizarEquipos),
    path('eliminar_equipos/<int:id>', views.eliminarEquipos),

    path('form_registrar_registro', views.mostrarFormRegistrarRegistro),
    path('registrar_registro', views.registrarRegistro),
    path('form_actualizar_registro/<int:id>', views.mostrarFormActualizarRegistro),
    path('actualizar_registro/<int:id>', views.actualizarRegistro),
    path('eliminar_registro/<int:id>', views.eliminarRegistro),


    path('form_registrar_fecha', views.mostrarFormRegistrarFecha),
    path('registrar_fecha', views.registrarFecha),
    path('form_actualizar_fecha/<int:id>', views.mostrarFormActualizarFecha),
    path('actualizar_fecha/<int:id>', views.actualizarFecha),
    path('eliminar_fecha/<int:id>', views.eliminarFecha),


    path('listar_historial', views.mostrarListarHistorial),
    path('historial_calendario', views.mostrarListarHistorialCalendario),



# USUARIO ----------------------------------------------------------------------------------

    path('menu_usuario', views.mostrarMenuUsuario),
    path('calendario_usuario', views.mostrarMenuCalendarioUsuario),

    path('usuario_actualizar_registro/<int:id>', views.mostrarUsuarioActualizarRegistro),
    path('actualizar_registro_usuario/<int:id>', views.actualizarRegistroUsuario),

    path('usuario_actualizar_fecha/<int:id>', views.mostrarUsuarioActualizarFecha),
    path('actualizar_fecha_usuario/<int:id>', views.actualizarFechaUsuario),
]

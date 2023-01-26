"""djangocrud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from tareas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.principal, name="principal"),
    path('registro/', views.registro, name="registro"),
    path('tareas/', views.tareas, name="tareas"),
    path('tareas_completadas/', views.tareas_completadas, name="tareas_completadas"),
    path('tareas/crear/', views.crear_tarea, name="crear_tareas"),
    path('tareas/<int:tarea_id>/', views.detalle_tarea, name="detalle_tareas"),
    path('tareas/<int:tarea_id>/completada', views.tarea_completada, name="tarea_completada"),
    path('tareas/<int:tarea_id>/borrada', views.tarea_borrada, name="tarea_borrada"),
    path('cerrar_sesion/', views.cerrar_sesion, name="cerrar_sesion"),
    path('iniciar_sesion/', views.iniciar_sesion, name="iniciar_sesion"),
]

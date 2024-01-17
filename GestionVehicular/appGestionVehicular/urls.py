
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('HME', views.BASE,name="BASE"),
    path('', views.LOGIN,name="LOGIN"),
    path('Personal', views.PERSONAL,name="PERSONAL"),
    path('Dependencias', views.DEPENDENCIAS,name="DEPENDENCIAS"),
    path('Mantenimiento', views.MANTENIMIENTO,name="MANTENIMIENTO"),
    path('Vehiculos', views.VEHICULOS,name="VEHICULOS"),
    path('Solicitud', views.SOLICITUD,name="SOLICITUD"),
    path('Ajustes', views.AJUSTES,name="AJUSTES"),
    path('Reporte', views.REPORTE,name="REPORTE"),
    path('ingreso_denuncias',views.DENUNCIAS,name="DENUNCIAS"),
    # inicio de sesion 
    path('accounts/', include('django.contrib.auth.urls')),
    ]

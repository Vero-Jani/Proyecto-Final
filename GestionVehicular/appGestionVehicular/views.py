from django.shortcuts import render

def BASE(request):
    return render(request,'base.html')

def LOGIN(request):
    return render(request,'login.html') 

def PERSONAL(request):
    return render(request,'personal.html')

def DEPENDENCIAS(request):
    return render(request,'dependencias.html')

def MANTENIMIENTO(request):
    return render(request,'mantenimiento.html')

def VEHICULOS(request):
    return render(request,'vehiculos.html') 

def SOLICITUD(request):
    return render(request,'solicitud.html')   

def AJUSTES(request):
    return render(request,'ajustes.html')                                                                       
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Personal,ReclamoSugerencia
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
@login_required
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('email')  # Asegúrate de que 'email' sea el nombre correcto en tu formulario
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('BASE')
        else:
            messages.error(request, 'Credenciales incorrectas. Por favor, inténtelo de nuevo.')

    return render(request, 'tu_template_de_login.html')

def BASE(request):
    return render(request,'base.html')

def LOGIN(request):
    return render(request,'login.html') 
 
# views.py
def PERSONAL(request):
    if request.method == 'POST':
        # Si la solicitud es POST, significa que se está enviando el formulario.
        cedula = request.POST.get('cedula')
        nombre = request.POST.get('nombre')
        telefono = request.POST.get('telefono')
        ciudad = request.POST.get('ciudad')
        fecha_nacimiento = request.POST.get('fecha_nacimiento')
        rango = request.POST.get('rango')
        dependencia = request.POST.get('dependencia')
        subcircuito = request.POST.get('subcircuito')

        # Crea una nueva instancia del modelo Personal con los datos del formulario
        Personal.objects.create(
            id=cedula,
            nombre=nombre,
            telefono=telefono,
            ciudad=ciudad,
            fecha_de_nacimiento=fecha_nacimiento,
            rango=rango,
            dependencia=dependencia,
            subcircuito_idsubcircuito=subcircuito
        )

        # Redirige a la misma página después de agregar el usuario
        return redirect('/Personal')

    # Este bloque de código se ejecuta solo si la solicitud no es de tipo POST
    # Obtiene todos los objetos Personal desde la base de datos
    personales = Personal.objects.all()
    
    # Renderiza la plantilla 'personal.html' con los objetos Personal y los pasa al contexto
    return render(request, 'personal.html', {'personales': personales})

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

def REPORTE(request):
   # Este bloque de código se ejecuta solo si la solicitud no es de tipo POST
    # Obtiene todos los objetos Personal desde la base de datos
    Reporte = ReclamoSugerencia.objects.all()
    
    # Renderiza la plantilla 'personal.html' con los objetos Personal y los pasa al contexto
    return render(request, 'reporte.html', {'Reporte': Reporte})                                     
   

def DENUNCIAS(request):
    if request.method == 'POST':
        # Si la solicitud es POST, significa que se está enviando el formulario.
        nombre = request.POST.get('nombres')
        apellido = request.POST.get('apellidos')
        circuito = request.POST.get('circuito')
        subcircuito = request.POST.get('subcircuito')
        reclamo_sugerencia = request.POST.get('reclamo_sugerencia')
        detalle = request.POST.get('detalle')
        contacto = request.POST.get('contacto')
        subcircuito = request.POST.get('subcircuito')

        # Crea una nueva instancia del modelo Personal con los datos del formulario
        ReclamoSugerencia.objects.create(
            nombres=nombre,
            apellidos=apellido,
            circuito=circuito,
            subcircuito=subcircuito,
            reclamo_sugerencia=reclamo_sugerencia,
            detalle=detalle,
            contacto=contacto,            
        )

        # Redirige a la misma página después de agregar el usuario
        return redirect('/')

                        
from django.shortcuts import render
from django.http import HttpResponse
from http.client import HTTPResponse
from .models import estudiante
# Create your views here.

infomation_users = [['Mathyas', 'Coronado'],
                    ['Josue', 'Quispe'], ['Camilo', 'Lopez']]


def index(request):
    return HttpResponse('Mi primera aplicacion Django')


def hola(request):
    lista_elementos = ['python', 'django', 'flask', 'js', 'php']
    return render(request, 'ejemplo2_django/hola.html', {
        'lista_elementos': lista_elementos,
    })


def hastaLuego(request):
    return render(request, 'ejemplo2_django/hastaLuego.html')


def usuariosInfo(request):
    if request.method == 'POST':
        nombreUsuario = request.POST.get('usuarioNombre')
        ApellidoUsuario = request.POST.get('usuarioApellido')
        CodigoUsuario = request.POST.get('usuarioCodigo')
        direccionUsuario = request.POST.get('usuarioDireccion')
        EmailUsuario = request.POST.get('usuarioEmail')
        estudiante(nombre=nombreUsuario, apellido=ApellidoUsuario, codigo=CodigoUsuario, direccion=direccionUsuario,email=EmailUsuario).save()
        return render(request, 'ejemplo2_django/usuariosInfo.html', {
            'usuarios': estudiante.objects.all(),
        })

    return render(request, 'ejemplo2_django/usuariosInfo.html', {
        'usuarios': estudiante.objects.all(),
    })

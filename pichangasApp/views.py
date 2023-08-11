from django.shortcuts import render
from pichangasApp.models import *
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from dateutil.parser import parse
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
import json


def ingresar(request):
    if request.method == 'POST':
        nombreUsuario = request.POST.get('nombreUsuario')
        passwordUsuario = request.POST.get('passwordUsuario')
        # validaciones de informacion
        usuario_registrado = 0  
        usuarios_totales = usuarios_app.objects.all()

        # usuarios_app.objects.filter(nombre=nombreUsuario).filter(psw_usuario=passwordUsuario)

        for usuario in usuarios_totales:
            if usuario.nombre == nombreUsuario and usuario.psw_usuario == passwordUsuario:
                usuario_registrado = 1

        if usuario_registrado == 1:
            return HttpResponseRedirect(reverse('pichangasApp:dashboard'))
        else:
            return render(request, 'pichangasApp/ingresar.html', {
                'mensaje': 'Los datos ingresados son incorrectos',
            })

    return render(request, 'pichangasApp/ingresar.html')


def dashboard(request):
    pichangas_equipo = []
    pichangas_locales = pichanga_app.objects.filter(equipo_local='1')
    for pichanga in pichangas_locales:
        pichangas_equipo.append(pichanga)
    pichangas_visitante = pichanga_app.objects.filter(equipo_visita='1')
    for pichanga in pichangas_visitante:
        pichangas_equipo.append(pichanga)
    return render(request, 'pichangasApp/dashboard.html', {
        'objPichanga': pichangas_equipo,
    })


def nuevaPichanga(request):
    if request.method == 'POST':
        fechaPichanga = request.POST.get('fechaPichanga')
        fechaPichanga = parse(fechaPichanga)
        equipoLocal = request.POST.get('equipoLocal')
        equipoVisita = request.POST.get('equipoVisita')
        pichanga_app(fecha=fechaPichanga, equipo_local=equipoLocal,
                     equipo_visita=equipoVisita).save()
        return HttpResponseRedirect(reverse('pichangasApp:dashboard'))
    return render(request, 'pichangasApp/nuevaPichanga.html', {
        'equipos_registrados': equipo_app.objects.all()

    })


def editarPichanga(request, ind):
    pichanga_editar = get_object_or_404(pichanga_app, id=ind)
    print(pichanga_editar.fecha)  # Verifica la fecha en la consola
    # Verifica el equipo local en la consola
    print(pichanga_editar.equipo_local)
    # Verifica el equipo visitante en la consola
    print(pichanga_editar.equipo_visita)

    if request.method == 'POST':
        equipoLocal = request.POST.get('equipoLocal')
        equipoVisita = request.POST.get('equipoVisita')
        # Cambiar a 'fecha' si es el nombre correcto en el modelo
        fechaPichanga = request.POST.get('fechaPichanga')
        pichanga_editar.equipo_local = equipoLocal
        pichanga_editar.equipo_visita = equipoVisita
        pichanga_editar.fecha = fechaPichanga
        pichanga_editar.save()
        return HttpResponseRedirect(reverse('pichangasApp:dashboard'))

    return render(request, 'pichangasApp/EditarPichanga.html', {
        'pichanga_info': pichanga_editar,
        'equipos_registrados': equipo_app.objects.all()
    })


def actualizar_estado(request, pichanga_id):
    if request.method == 'POST':
        # Obtener el nuevo estado desde la solicitud POST
        data = json.loads(request.body)
        nuevo_estado = data.get('nuevo_estado')

        # Obtener la pichanga desde la base de datos usando su ID
        pichanga = get_object_or_404(pichanga_app, id=pichanga_id)

        # Actualizar el estado de la pichanga en la base de datos
        pichanga.estadoPichanga = nuevo_estado
        pichanga.save()

        return JsonResponse({'mensaje': 'Estado actualizado exitosamente.'})

    return JsonResponse({'error': 'Método de solicitud no válido.'}, status=400)


def eliminar_pichanga(request, pichanga_id):
    # Obtén la pichanga por su ID o muestra un error 404 si no existe
    pichanga = get_object_or_404(pichanga_app, id=pichanga_id)

    # Elimina la pichanga
    pichanga.delete()

    # Redirige a la vista dashboard después de eliminar
    return redirect('pichangasApp:dashboard')


def verPichanga(request, pichanga_id):
    pichanga = get_object_or_404(pichanga_app, id=pichanga_id)

    return render(request, 'pichangasApp/verPichanga.html', {
        'pichanga': pichanga
    })


def crearCuenta(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        password = request.POST.get('password')
        celularusu = request.POST.get('celularusu')
        equipousu = request.POST.get('equipousu')
        usuarios_app(nombre=usuario, psw_usuario=password,
                     celular=celularusu, equipo=equipousu).save()
        return HttpResponseRedirect(reverse('pichangasApp:ingresar'))
    return render(request, 'pichangasApp/crearCuenta.html', {
        'equipos_registrados': equipo_app.objects.all()
    })

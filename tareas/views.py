from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .formularios import TareasForm
from .models import Tarea
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.


def principal(request):
    return render(request, 'principal.html')


def registro(request):
    if request.method == 'GET':
        return render(request, 'registro.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect("tareas")
            except:
                return render(request, 'registro.html', {
                    'form': UserCreationForm,
                    "error": "usuario ya existe"
                })
        return render(request, 'registro.html', {
            'form': UserCreationForm,
            "error": "contraseñas nos coinciden"
        })

@login_required
def tareas(request):
    tareas = Tarea.objects.filter(
        usuario=request.user, completada__isnull=True)
    return render(request, "tareas.html", {'tareas': tareas})

@login_required
def tareas_completadas(request):
    tareas = Tarea.objects.filter(
        usuario=request.user, completada__isnull=False).order_by('-completada')
    return render(request, "tareas.html", {'tareas': tareas})

@login_required
def detalle_tarea(request, tarea_id):
    if request.method == 'GET':
        tarea = get_object_or_404(Tarea, pk=tarea_id, usuario=request.user)
        form = TareasForm(instance=tarea)
        return render(request, 'detalle_tarea.html', {
            "tarea": tarea,
            "form": form
        })
    else:
        try:
            tarea = get_object_or_404(Tarea, pk=tarea_id, usuario=request.user)
            form = TareasForm(request.POST, instance=tarea)
            form.save()
            return redirect('tareas')
        except ValueError:
            return render(request, 'detalle_tarea.html', {
                "tarea": tarea,
                "form": form,
                'error': 'Error actualizando la tarea'
            })

@login_required
def tarea_completada(request, tarea_id):
    tarea = get_object_or_404(Tarea, pk=tarea_id, usuario=request.user)
    if request.method == 'POST':
        tarea.completada = timezone.now()
        tarea.save()
        return redirect('tareas')

@login_required
def tarea_borrada(request, tarea_id):
    tarea = get_object_or_404(Tarea, pk=tarea_id, usuario=request.user)
    if request.method == 'POST':
        tarea.delete()
        return redirect('tareas')

@login_required
def crear_tarea(request):
    if request.method == 'GET':
        return render(request, 'crear_tarea.html', {
            'form': TareasForm
        })
    else:
        try:
            formulario = TareasForm(request.POST)
            nueva_tarea = formulario.save(commit=False)
            nueva_tarea.usuario = request.user
            nueva_tarea.save()
            return redirect('tareas')
        except:
            return render(request, 'crear_tarea.html', {
                'form': TareasForm,
                'Error': 'ingrese datos validos'
            })

@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('principal')


def iniciar_sesion(request):
    if request.method == 'GET':
        return render(request, "iniciar_sesion.html", {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request, "iniciar_sesion.html", {
                'form': AuthenticationForm,
                'error': 'El nombre se usuario o la contraseña es incorrecta'
            })

        login(request, user)
        return redirect('tareas')

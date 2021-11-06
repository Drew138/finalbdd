from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
from .models import *
from django.contrib import messages
# Create your views here.


def ClaseView(request, *args, **kwargs):
    print(request)
    if 'pk' in kwargs:
        pk = kwargs['pk']
        instance = get_object_or_404(Clase, id=pk)
        if request.method == 'POST':
            form = ClaseForm(request.POST, instance=instance)
            if 'crear' in request.POST:
                form = ClaseForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('/clase/')
                else:
                    messages.error(request, "Error")
            elif 'borrar' in request.POST:
                instance.delete()
                return redirect('/')
            elif 'actualizar' in request.POST:
                if form.is_valid():
                    form.save()
                    return redirect(f'/clase/{pk}/')
            elif 'buscar' in request.POST:
                pk = request.POST.get('primary_key', None) or pk
                return redirect(f'/clase/{pk}/')
            elif 'regresar' in request.POST:
                return redirect('/')
        else:
            form = ClaseForm(instance=instance)
            # print(form)
    elif request.method == 'POST':
        # if request.POST["equipos"]
        if 'crear' in request.POST:
            form = ClaseForm(request.POST)
            print(form.errors)
            if form.is_valid():
                form.save()
                return redirect('/clase/')
            else:
                messages.error(request, "Error")
        elif 'buscar' in request.POST:
            pk = request.POST.get('primary_key')
            if pk is None:
                messages.error(request, "Error")
                return redirect('/clase/')
            else:
                return redirect(f'/clase/{pk}/')

    else:
        form = ClaseForm()
    context = {'form': form}

    return render(request, 'util/form.html', context)


def CalendarioView(request, *args, **kwargs):
    if 'pk' in kwargs:
        instance = get_object_or_404(Clase, id=kwargs['pk'])

        if request.method == 'POST':
            form = CalendarioForm(request.POST, instance=instance)
            if form.is_valid():
                form.save()
            else:
                messages.error(request, "Error")
        else:
            form = CalendarioForm(instance=instance)
    else:
        form = CalendarioForm()

    context = {'form': form}

    return render(request, 'util/form.html', context)


def ZonaView(request, *args, **kwargs):

    if 'pk' in kwargs:
        instance = get_object_or_404(Zona, id=kwargs['pk'])

        if request.method == 'POST':
            form = ZonaForm(request.POST, instance=instance)
            if form.is_valid():
                form.save()
            else:
                messages.error(request, "Error")
        else:
            form = ZonaForm(instance=instance)
    else:
        form = ZonaForm()
    context = {'form': form}

    return render(request, 'util/form.html', context)


def RutinaView(request, args, **kwargs):

    if 'pk' in kwargs:
        instance = get_object_or_404(Rutina, id=kwargs['pk'])

        if request.method == 'POST':
            form = RutinaForm(request.POST, instance=instance)
            if form.is_valid():
                form.save()
            else:
                messages.error(request, "Error")
        else:
            form = RutinaForm(instance=instance)
    else:
        form = RutinaForm()
    context = {'form': form}

    return render(request, 'util/form.html', context)

    form = RutinaForm

    context = {'form': form}

    return render(request, 'util/form.html', context)


def PersonaView(request, *args, **kwargs):
    if 'pk' in kwargs:
        instance = get_object_or_404(Clase, id=kwargs['pk'])

        if request.method == 'POST':
            form = PersonaForm(request.POST, instance=instance)
            if form.is_valid():
                form.save()
            else:
                messages.error(request, "Error")
        else:
            form = PersonaForm(instance=instance)
    else:
        form = PersonaForm()

    context = {'form': form}

    return render(request, 'util/form.html', context)


def EquipoDeEntrenamientoView(request, *args, **kwargs):
    if 'pk' in kwargs:
        instance = get_object_or_404(Clase, id=kwargs['pk'])

        if request.method == 'POST':
            form = EquipoDeEntrenamientoForm(request.POST, instance=instance)
            if form.is_valid():
                form.save()
            else:
                messages.error(request, "Error")
        else:
            form = EquipoDeEntrenamientoForm(instance=instance)
    else:
        form = EquipoDeEntrenamientoForm()

    context = {'form': form}

    return render(request, 'util/form.html', context)


def Home(request):

    return render(request, 'home/home.html')

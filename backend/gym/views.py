from django.shortcuts import render
from .forms import *
# Create your views here.


def ClaseView(request):

    form = ClaseForm

    context = {'form': form}

    return render(request, 'util/form.html', context)


def CalendarioView(request):

    form = CalendarioForm

    context = {'form': form}

    return render(request, 'util/form.html', context)


def ZonaView(request):

    form = ZonaForm

    context = {'form': form}

    return render(request, 'util/form.html', context)


def RutinaView(request):

    form = RutinaForm

    context = {'form': form}

    return render(request, 'util/form.html', context)


def PersonaView(request):

    form = PersonaForm

    context = {'form': form}

    return render(request, 'util/form.html', context)


def EquipoDeEntrenamientoView(request):

    form = EquipoDeEntrenamientoForm

    context = {'form': form}

    return render(request, 'util/form.html', context)


def Home(request):

    return render(request, 'home/home.html')

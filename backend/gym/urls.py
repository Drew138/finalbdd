from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home, name='home'),
    path('clase/', views.ClaseView, name='clases'),
    path('calendario/', views.CalendarioView, name='calendario'),
    path('zona/', views.ZonaView, name='zona'),
    path('rutina/', views.RutinaView, name='rutina'),
    path('persona/', views.PersonaView, name='persona'),
    path('equipo/', views.EquipoDeEntrenamientoView, name='equipo'),
]

from . import views
from django.urls import path

app_name = 'pichangasApp'

urlpatterns = [

    path('', views.ingresar, name='ingresar'),  
    path('dashboard', views.dashboard, name='dashboard'),
    path('nuevaPichanga', views.nuevaPichanga, name='nuevaPichanga'),
    path('editarPichanga/<str:ind>', views.editarPichanga, name='editarPichanga'),
    path('crearCuenta', views.crearCuenta, name='crearCuenta'),
    path('eliminar_pichanga/<int:pichanga_id>/', views.eliminar_pichanga, name='eliminarPichanga'),
    path('actualizar_estado/<int:pichanga_id>/', views.actualizar_estado, name='actualizar_estado'),
    path('verPichanga/<int:pichanga_id>/', views.verPichanga, name='verPichanga'),


]
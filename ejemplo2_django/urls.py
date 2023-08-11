from . import views
from django.urls import path 

app_name = 'ejemplo2_django'

urlpatterns = [
    
    path('', views.index,name='index'),
    path('hola', views.hola,name='hola'),
    path('hastaLuego', views.hastaLuego,name='hastaLuego'),
    path('usuariosInfo', views.usuariosInfo,name='usuariosInfo'),
]

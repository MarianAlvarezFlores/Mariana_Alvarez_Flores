from django.urls import path
from . import views 

app_name = "Clase"

urlpatterns = [
    path('', views.home, name='home'),
    path('comision/create/', views.create, name='comision_create'),
    path ('comision/home/', views.comision_home, name = 'comision_home'), 
    path('estudiante/', views.estudiante_home, name='estudiante_home'),
    path('estudiante/create/', views.estudiante_create, name='estudiante_create'),
    path('profesor/', views.profesor_home, name='profesor_home'),
    path('profesor/create/', views.profesor_create, name='profesor_create'),
    path('curso/', views.curso_home, name='curso_home'),
    path('curso/create/', views.curso_create, name='curso_create'), 
]
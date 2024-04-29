from django.urls import path
from . import views 

app_name = "Clase"

urlpatterns = [
    path ("", views.home, name = "home"),
]
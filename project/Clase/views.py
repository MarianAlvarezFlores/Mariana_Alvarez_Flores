from django.shortcuts import render, redirect

from . import models

from .forms import ComisionForm, EstudianteForm, ProfesorForm, CursoForm


def home(request):
    query = models.Comision.objects.all()
    context = {"comisiones": query}
    return render(request, "Comision/index.html", context)

def create(request):
    if(request.method == "POST"):
        form = ComisionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Clase:comision_create")
        else:
            form2 = ComisionForm()
            return render(request, "Comision/create.html", {"error": form.errors, "form": form2})
    else:
        form = ComisionForm()
        return render(request, "Comision/create.html", {"form": form})
    
def estudiante_home(request):
    query = models.Estudiante.objects.all()
    context = {"estudiantes": query}
    return render(request, "Estudiante/index.html", context)
    
def estudiante_create(request):
    if(request.method == "POST"):
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Clase:estudiante_home")
        else:
            form2 = EstudianteForm()
            return render(request, "Estudiante/create.html", {"error": form.errors, "form": form2})
    else:
        form = EstudianteForm()
        return render(request, "Estudiante/create.html", {"form": form})
    
def profesor_home(request):
    query = models.Profesor.objects.all()
    context = {"profesores": query}
    return render(request, "Profesor/index.html", context)

def profesor_create(request):
    if request.method == "POST":
        form = ProfesorForm (request.POST)
        if form.is_valid():
            form.save()
            return redirect("Clase:profesor_home")
        else:
            return render(request, "Profesor/create.html", {"form": form, "error": form.errors})
    else:
        form = ProfesorForm()
        return render(request, "Profesor/create.html", {"form": form})

def curso_home(request):
    query = models.Curso.objects.all()
    context = {"cursos": query}
    return render(request, "Curso/index.html", context)

def curso_create(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Clase:curso_home")
        else:
            return render(request, "Curso/create.html", {"form": form, "error": form.errors})
    else:
        form = CursoForm()
        return render(request, "Curso/create.html", {"form": form})

def comision_home(request):
    query = models.Comision.objects.all()
    context = {"comisiones": query}
    return render(request, "Comision/index.html", context)

def comision_create(request):
    if request.method == "POST":
        form = ComisionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Clase:comision_home")  # Redirige a la vista de listado de comisiones
        else:
            return render(request, "Comision/create.html", {"form": form, "error": form.errors})
    else:
        form = ComisionForm()
        return render(request, "Comision/create.html", {"form": form})
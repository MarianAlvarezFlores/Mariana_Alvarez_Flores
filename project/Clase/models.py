from django.db import models

class Curso (models.Model):
    nombre = models.CharField (max_length=100)

    def __str__(self) -> str:
        return self.nombre

class Estudiante (models.Model):
    nombre = models.CharField (max_length=200)
    curso = models.ForeignKey (Curso, on_delete= models.SET_NULL, null= True, blank= True)
    def __str__(self) -> str:
        return self.nombre
    
    class Meta:
        verbose_name="estudiante"
        verbose_name_plural = "estudiantes"

class Profesor (models.Model):
    nombre = models.CharField (max_length=200)

    class Meta:
        verbose_name="profesor/a"
        verbose_name_plural = "profesores/as"

    def __str__(self) -> str:
        return self.nombre

class Comision (models.Model):
    nombre = models.PositiveIntegerField (unique= True)
    curso = models.ForeignKey (Curso, on_delete = models.SET_NULL, null= True, blank= True)
    profesor = models.ForeignKey (Profesor, on_delete= models.SET_NULL, null= True, blank= True)
    estudiante = models.ManyToManyField (Estudiante)
    
    def __str__(self) -> str:
        return str (self.nombre)
    
    def mostrar_comisiones(self, request):
        comisiones = Comision.objects.all()
        return (request, 'comisiones.html', {'comisiones': comisiones})
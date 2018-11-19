from django.contrib import admin
from registro.models import Alumno, Grado, Seccion, Materia, Profesor, RegistroAlumno, RegistroProfesor

#Registramos nuestras clases principales.
admin.site.register(Alumno)
admin.site.register(Grado)
admin.site.register(Seccion)
admin.site.register(Materia)
admin.site.register(Profesor)
admin.site.register(RegistroAlumno)
admin.site.register(RegistroProfesor)


# Register your models here.

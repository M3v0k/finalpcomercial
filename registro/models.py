from django.db import models
from django.contrib import admin


#tabla profesor

class Profesor(models.Model):

    nombre  =   models.CharField(max_length=60, verbose_name="Nombre")
    direcion  =   models.CharField(max_length=200, verbose_name="Direccion")

    class Meta:
                verbose_name="Profesor"
                verbose_name_plural="Profesors"
                ordering = ["-nombre"]

    def __str__(self): #devuelve el nombre del proyecto
        return self.nombre


#tabla alumnos
class Alumno(models.Model):

    nombre  =   models.CharField(max_length=60, verbose_name="Nombre")
    apellido  =   models.CharField(max_length=200, verbose_name="Apellido")

    class Meta:
                verbose_name="Alumno"
                verbose_name_plural="Alumnos"
                ordering = ["-nombre"]

    def __str__(self): #devuelve el nombre del proyecto
        return self.nombre

class Materia(models.Model):

    nombre  =   models.CharField(max_length=60, verbose_name="Nombre")
    creditos  =   models.CharField(max_length=200, verbose_name="Creditos")

    class Meta:
                verbose_name="Materia"
                verbose_name_plural="Materias"
                ordering = ["-nombre"]

    def __str__(self): #devuelve el nombre del proyecto
        return self.nombre

#se creo la tabla seccion para que se pueda seleccionar al momento del registro
class Seccion(models.Model):

    nombre  =   models.CharField(max_length=60, verbose_name="Nombre")

    class Meta:
                verbose_name="Seccion"
                verbose_name_plural="Seccions"
                ordering = ["-nombre"]

    def __str__(self): #devuelve el nombre del proyecto
        return self.nombre


#tabla donde se crea la relacion , con seccion luego con la tabla materia que es de muchos a  muchos
class Grado(models.Model):

    nombre = models.CharField(max_length=100)
    seccion = models.ForeignKey(Seccion,on_delete=models.CASCADE,related_name="keyseccion")
    materia = models.ManyToManyField(Materia,verbose_name="Materia",related_name="keymateria")

    class Meta:
                verbose_name="Grado"
                verbose_name_plural="Grados"
                ordering = ["-nombre"]

    def __str__(self):
        return self.nombre

#primera tabla de regitro donde se guarda el alumno y su rescpectivo grado, la relacion es de uno a muchos ya que un alumno solo puede estar en un solo grado

class RegistroAlumno(models.Model):

    alumnos = models.ForeignKey(Alumno,on_delete=models.CASCADE)
    grados = models.ForeignKey(Grado,on_delete=models.CASCADE)

    class Meta:
                verbose_name="RegistroAlumno"
                verbose_name_plural="RegistroAlumnos"

    def __str__(self):
        return self.alumno

#segunda tabla donde se le asignan al profesor los grados a cargo y materia que impratira

class RegistroProfesor(models.Model):

    grados = models.ManyToManyField(Grado,verbose_name="Grado")
    materias = models.ManyToManyField(Materia,verbose_name="Materia")

    class Meta:
                verbose_name="RegistroProfesor"
                verbose_name_plural="RegistroProfesors"

    def __str__(self):
        return self.grado

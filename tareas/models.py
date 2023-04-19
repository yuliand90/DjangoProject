from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tarea(models.Model):
    ALTA = '1'
    NORMAL = '2'
    BAJA = '3'
   
    PRIORIDAD_TAREA = (
        (ALTA, 'Alta'),
        (NORMAL, 'Normal'),
        (BAJA, 'Baja'),
    )

    nombre = models.CharField(max_length=100, help_text="Nombre de la tarea")
    descripcion = models.TextField(help_text="Descripción de la tarea")
    responsable = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_limite = models.DateTimeField(auto_now_add=True,  help_text="Fecha limite")

class Persona(models.Model):
    dni = models.CharField(max_length = 8,primary_key = True)
    apellidoPaterno =  models.CharField(max_length = 35)
    apellidoMaterno =  models.CharField(max_length = 35)
    nombres =  models.CharField(max_length = 35)
    fechaNacimiento =  models.DateField()
    sexos = [
        ('F','Femenino'),
        ('M','Masculino')
    ]
    
    sexo = models.CharField(max_length = 1,choices = sexos,default = 'M')
  
from django.db import models


class Usuario(models.Model):
    nombre_usuario = models.TextField(max_length=20)
    password_usuario = models.TextField(max_length=20)


class Buque(models.Model):
    nombre_buque = models.TextField(max_length=20)
    horometro = models.IntegerField(null=False)


class Departamento(models.Model):
    nombre_departamento = models.TextField(max_length=20)


class Sistema(models.Model):
    nombre_sistema = models.TextField(max_length=20)


class Equipo(models.Model):
    nombre_equipo = models.TextField(max_length=20)
    hora_standar = models.IntegerField(null=False)

class Equipos(models.Model):
    nom_equipo = models.TextField(max_length=50)




class Registro(models.Model):
    buque = models.ForeignKey(Buque, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    sistema = models.ForeignKey(Sistema, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    nombre_texto= models.TextField(max_length=300)
    nombre_prioridad = models.TextField(max_length=20)
    ultimo_mantenimiento = models.DateField()
    ultimo_horometro = models.IntegerField(null=False)
    comentario = models.TextField(max_length=500)
    estado_ejecucion = models.TextField(max_length=50)
    


class Fecha(models.Model):
    buque = models.ForeignKey(Buque, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    sistema = models.ForeignKey(Sistema, on_delete=models.CASCADE)
    equipos = models.ForeignKey(Equipos, on_delete=models.CASCADE)
    actividad = models.TextField(max_length=50)
    prioridad = models.TextField(max_length=50)
    ult_mantenimiento = models.DateField(max_length=50)
    texto_comentario = models.TextField(max_length=500)
    ejecucion = models.TextField(max_length=50)
    frecuencia = models.IntegerField(null=False)



class Historial(models.Model):
    buque = models.ForeignKey(Buque, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    sistema = models.ForeignKey(Sistema, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    descripcion_historial = models.TextField(max_length=200)
    registro_horometro = models.IntegerField()
    fecha_hora_historial = models.DateTimeField()


class HistorialCal (models.Model):
    buque = models.ForeignKey(Buque, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    sistema = models.ForeignKey(Sistema, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    descripcion_actividad = models.TextField(max_length=200)
    descripcion_frecuencia = models.IntegerField()
    fecha_historial = models.DateTimeField()


# Create your models here.w

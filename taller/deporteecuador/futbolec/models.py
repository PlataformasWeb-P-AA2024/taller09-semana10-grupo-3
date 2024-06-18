from django.db import models

# Create your models here.

class Equipo(models.Model):
    nombre = models.CharField("Nombre del Equipo de Futbol",max_length=100)
    siglas = models.CharField("Siglas",max_length=30)
    usernameTwi = models.CharField("Username de Twitter",max_length=30)  # el campo puede

    def __str__(self):
        return "%s - %s - %s" % (self.nombre,
                self.siglas,
                self.usernameTwi)


class Jugador(models.Model):
    nombre = models.CharField("Nombre del Jugador",max_length=30)
    posicion = models.CharField(max_length=30)
    numeroCamiseta = models.IntegerField()
    sueldo = models.IntegerField()
    equipo = models.ForeignKey(Equipo,on_delete=models.CASCADE)

    def __str__(self):
        return "%s - %s - %d - %d" % (self.nombre,
        		self.posicion,
        		self.numeroCamiseta,
        		self.sueldo)


class Campeonato(models.Model):
    nombreCampeonato = models.CharField("Nombre del Campeonato", max_length=30)
    nombreAuspiciante = models.CharField("Nombre del Auspiciante",max_length=200)

    def __str__(self):
        return "%s - %s" % \
                (self.nombreCampeonato, self.nombreAuspiciante)


class CampeonatoEquipos(models.Model):
    anio = models.IntegerField()
    equipo = models.ForeignKey(Equipo,on_delete=models.CASCADE)
    campeonato = models.ForeignKey(Campeonato,on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % \
                (self.anio)
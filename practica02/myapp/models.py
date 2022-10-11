import datetime
from django.db import models

# Create your models here.

#Autor
class Autor(models.Model):
    idautor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

#Libro
class Libro(models.Model):
    idlibro = models.AutoField(primary_key=True)
    codigo = models.IntegerField()
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor,on_delete=models.CASCADE)
    isbn = models.CharField(max_length=30)
    editorial = models.CharField(max_length=60)
    numpags = models.SmallIntegerField()

    def __str__(self):
        return self.titulo

#Usuario
class Usuario(models.Model):
    idusuario = models.AutoField(primary_key=True)
    numusuario = models.IntegerField()
    nif = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

#Prestamos
class Prestamo(models.Model):
    idprestamo = models.AutoField(primary_key=True)
    idbook = models.ForeignKey(Libro,on_delete=models.CASCADE)
    iduser = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    fecprestamo = models.DateField(default=datetime.date.today)
    fecdevolucion = models.DateField()

    def get_usuario(self):
        return ", ".join([p.nombre for p in self.iduser.all()])

    def get_libro(self):
        return ", ".join([p.titulo for p in self.idbook.all()])

    def __str__(self):
        return self.iduser.nombre

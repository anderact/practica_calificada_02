from django.contrib import admin

# Register your models here.
from .models import Autor, Libro, Usuario, Prestamo

admin.site.register([Autor, Libro, Usuario, Prestamo])
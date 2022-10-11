from django.shortcuts import render

# Create your views here.
from .models import Autor, Libro, Prestamo, Usuario

def all_Prestamo(request):
    
    #prestamos=Prestamo.objects.all()
    prestamos=Prestamo.objects.raw('select idprestamo, codigo, titulo, myapp_prestamo.iduser_id, fecprestamo, fecdevolucion from myapp_prestamo full outer join myapp_libro ON myapp_libro.idlibro = myapp_prestamo.idbook_id')

    #template a usar
    template_name='index.html'
    
    context={
        'prestamo':prestamos,
        
    }
    return render(request,template_name,context)
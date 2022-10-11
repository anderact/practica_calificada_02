from django.urls import path
from .views import all_Prestamo

urlpatterns = [
    path('',all_Prestamo,name='all_Prestamo')
]
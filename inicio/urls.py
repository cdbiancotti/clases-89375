from django.urls import path
from inicio.views import inicio, prueba_bucle

app_name = 'inicio'

urlpatterns = [
    path('', inicio, name='inicio'),
    path('prueba-bucle/', prueba_bucle, name='prueba_bucle'),
]

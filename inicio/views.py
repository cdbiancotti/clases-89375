from django.shortcuts import render
from django.http import HttpResponse

# v1
# def inicio(request):
#     return HttpResponse("<h1>Hola Mundo</h1>")

# v2
def inicio(request):
    
    # return render(request, 'inicio.html', {})
    return render(request, 'inicio/inicio.html')

def prueba_bucle(request):

    numeros = list(range(1, 11))

    return render(request, 'inicio/prueba_bucle.html', {'datos': numeros})
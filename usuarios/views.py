from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import login
from usuarios.forms import InicioSesion, FormularioCreacion, EditarPerfil, FormularioCambioContrasenia
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from usuarios.models import InfoExtra

def iniciar_sesion(request):

    if request.method == "POST":
        formulario = InicioSesion(request, data=request.POST)
        if formulario.is_valid():
            
            user = formulario.get_user()
            
            login(request, user)
            
            InfoExtra.objects.get_or_create(user=user)
            
            return redirect('inicio:inicio')
    else:
        formulario = InicioSesion()
        
    return render(request, 'usuarios/iniciar_sesion.html', {'formulario': formulario})

def registrarse(request):
    
    if request.method == "POST":
        formulario = FormularioCreacion(request.POST)
        if formulario.is_valid():
            formulario.save()
            
            return redirect('usuarios:iniciar_sesion')
    else:
        formulario = FormularioCreacion()
        
    return render(request, 'usuarios/registro.html', {'formulario': formulario})

def perfil(request):
    return render(request, 'usuarios/perfil.html')

def editar_perfil(request):
    
    if request.method == "POST":
        formulario = EditarPerfil(request.POST, instance=request.user)
        if formulario.is_valid():
            
            if formulario.cleaned_data.get('fecha_nacimiento'):
                request.user.infoextra.fecha_nacimiento = formulario.cleaned_data.get('fecha_nacimiento')
                request.user.infoextra.save()
            
            formulario.save()
            return redirect('usuarios:perfil')
    else:
        formulario = EditarPerfil(instance=request.user)
    
    return render(request, 'usuarios/editar_perfil.html', {'formulario': formulario})


class CambiarContrasenia(PasswordChangeView):
    template_name = 'usuarios/cambiar_contrasenia.html'
    success_url = reverse_lazy('usuarios:perfil')
    form_class = FormularioCambioContrasenia
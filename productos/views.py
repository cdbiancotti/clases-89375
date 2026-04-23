from django.shortcuts import render, redirect
from productos.models import JabonLiquido
from productos.forms import FormularioCreacionJabonLiquido, FormularioCreacionJabonLiquidoCBV
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def listado(request):
    
    productos = JabonLiquido.objects.all()
    
    return render(request, 'productos/listado.html', {'productos': productos})

@login_required
def crear_jabon_liquido(request):
    
    # print('POST: ', request.POST)
    # print('GET: ', request.GET)
    
    if request.method == 'POST':
        formulario = FormularioCreacionJabonLiquido(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            jabon_liquido = JabonLiquido(marca=info.get('marca'), descripcion=info.get('descripcion'), fecha=info.get('fecha'))
            jabon_liquido.save()
            return redirect('productos:listado_jabon_liquido')
    else:
        formulario = FormularioCreacionJabonLiquido()
    
    return render(request, 'productos/crear.html', {'formulario': formulario})

def detalle_jabon_liquido(request, clave_primaria):
    
    jabon_liquido = JabonLiquido.objects.get(id=clave_primaria)
    
    return render(request, 'productos/detalle.html', {'producto': jabon_liquido})

class BorrarJabonLiquido(LoginRequiredMixin, DeleteView):
    model = JabonLiquido
    template_name = "productos/borrado.html"
    success_url = reverse_lazy('productos:listado_jabon_liquido')

class ActualizarJabonLiquido(LoginRequiredMixin, UpdateView):
    model = JabonLiquido
    template_name = "productos/actualizar.html"
    success_url = reverse_lazy('productos:listado_jabon_liquido')
    # fields = ['marca', 'descripcion']
    # fields = ['marca', 'descripcion', 'fecha']
    # fields = '__all__'
    form_class = FormularioCreacionJabonLiquidoCBV
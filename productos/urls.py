from django.urls import path
from productos.views import listado, crear_jabon_liquido, detalle_jabon_liquido, BorrarJabonLiquido, ActualizarJabonLiquido

app_name = 'productos'

urlpatterns = [
    path('', listado, name='listado_jabon_liquido'),
    path('crear/', crear_jabon_liquido, name='crear_jabon_liquido'),
    path('<clave_primaria>/', detalle_jabon_liquido, name='detalle_jabon_liquido'),
    path('<pk>/borrar/', BorrarJabonLiquido.as_view(), name='borrar_jabon_liquido'),
    path('<pk>/actualizar/', ActualizarJabonLiquido.as_view(), name='actualizar_jabon_liquido'),
]

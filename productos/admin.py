from django.contrib import admin
from productos.models import JabonLiquido

# admin.site.register(JabonLiquido)

class JabonLiquidoAdmin(admin.ModelAdmin):
    search_fields = ['marca']
    list_display = ['marca', 'descripcion']
    list_filter = ['fecha']


admin.site.register(JabonLiquido, JabonLiquidoAdmin)
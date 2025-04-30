# apps/empresa/admin.py
from django.contrib import admin
# apps/empresa/sena_empresa/admin.py
from django.contrib import admin
from .models import SenaEmpresa  # Importación relativa: .models está en el mismo directorio

# Registrar el modelo SenaEmpresa en el admin
@admin.register(SenaEmpresa)
class SenaEmpresaAdmin(admin.ModelAdmin):
    list_display = ('id_sena', 'nombre', 'num_factura')
    search_fields = ('nombre',)
    list_filter = ('nombre',)
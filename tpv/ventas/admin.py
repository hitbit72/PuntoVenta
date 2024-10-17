from django.contrib import admin
from ventas.models import Cliente, Producto

# Register your models here.

class ClientesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'codigo')
    search_fields = ('nombre', 'codigo')
    readonly_fields = ('created', 'updated')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'descripcion', 'imagen', 'costo', 'cantidad')
    search_fields = ('descripcion', 'codigo')
    readonly_fields = ('created', 'updated')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Cliente, ClientesAdmin)
admin.site.register(Producto, ProductoAdmin)
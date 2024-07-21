from django.contrib import admin

# Tienda Pipi by Mica Lira

from .models import *

class ProveedorMercaderiaAdm(admin.ModelAdmin):
    list_display = ("nombre","pagina","email","costoenvio","demoraenvio")
    list_filter = ("nombre",)
    
class TiendaMayoristaAdm(admin.ModelAdmin):
    list_display = ("nombre","apellido","telefono","dni","email")
    list_filter = ("nombre",)
    
class TiendaMinoristaAdm(admin.ModelAdmin):
    list_display = ("nombre","apellido","telefono","dni","email")
    list_filter = ("nombre",)
    
class ProductosMinoristaAdm(admin.ModelAdmin):
    list_display = ("nombre","valor","cantidad","tamaño","peso")
    list_filter = ("nombre",)
    
class ProductosMayoristaAdm(admin.ModelAdmin):
    list_display = ("nombre","valor","cantidad","tamaño","peso")
    list_filter = ("nombre",)    

class EmpresaEnvioClientesAdm(admin.ModelAdmin):
    list_display = ("nombre","pagina","email","costoenvio","demoraenvio")
    list_filter = ("nombre",)

class EntregableProductoAdm(admin.ModelAdmin):
    list_display = ("nombre","provincia","empresaenvio","fechaEntrega","entregado")
    list_filter = ("nombre",)
    
admin.site.register(TiendaMayorista,TiendaMayoristaAdm)
admin.site.register(TiendaMinorista,TiendaMinoristaAdm)
admin.site.register(ProductosMinorista,ProductosMinoristaAdm)
admin.site.register(ProductosMayorista,ProductosMayoristaAdm)
admin.site.register(ProveedorMercaderia, ProveedorMercaderiaAdm)
admin.site.register(EmpresaEnvioClientes,EmpresaEnvioClientesAdm)
admin.site.register(EntregableProducto,EntregableProductoAdm)

from django.urls import path, include
from .views import *
from . import views

# Tienda Pipi by Mica Lira

urlpatterns = [
    path('', home, name="home"),
    path('acerca/', acerca, name="acerca"),
    
#___tiendaMinorista app TiendaPipi by Mica Lira
    path('tiendaMinorista/', tiendaMinorista, name="tiendaMinorista"),
    path('tiendaMinoristaForm/', tiendaMinoristaForm, name="tiendaMinoristaForm"),   
    path('buscarTiendaMinorista/', buscarTiendaMinorista, name="buscarTiendaMinorista"),
    path('encontrarTiendaMinorista/', encontrarTiendaMinorista, name="encontrarTiendaMinorista"),
    path('tiendaMinoristaUpdate/<id_tiendaMinorista>/', tiendaMinoristaUpdate, name="tiendaMinoristaUpdate"),
    path('tiendaMinoristaDelete/<id_tiendaMinorista>/', tiendaMinoristaDelete, name="tiendaMinoristaDelete"),

#___productosMinorista app TiendaPipi by Mica Lira
    path('productosMinorista/', ProductosMinoristaList.as_view(), name="productosMinorista"),
    path('productosMinoristaCreate/', ProductosMinoristaCreate.as_view(), name="productosMinoristaCreate"),
    path('productosMinoristaUpdate/<int:pk>/', ProductosMinoristaUpdate.as_view(), name="productosMinoristaUpdate"),
    path('productosMinoristaDelete/<int:pk>/', ProductosMinoristaDelete.as_view(), name="productosMinoristaDelete"),

#___tiendaMayorista app TiendaPipi by Mica Lira
    path('tiendaMayorista/', TiendaMayoristaList.as_view(), name="tiendaMayorista"),
    path('tiendaMayoristaCreate/', TiendaMayoristaCreate.as_view(), name="tiendaMayoristaCreate"),
    path('tiendaMayoristaUpdate/<int:pk>/', TiendaMayoristaUpdate.as_view(), name="tiendaMayoristaUpdate"),
    path('tiendaMayoristaDelete/<int:pk>/', TiendaMayoristaDelete.as_view(), name="tiendaMayoristaDelete"),
    
#___productosMayorista app TiendaPipi by Mica Lira
    path('productosMayorista/', ProductosMayoristaList.as_view(), name="productosMayorista"),
    path('productosMayoristaCreate/', ProductosMayoristaCreate.as_view(), name="productosMayoristaCreate"),
    path('productosMayoristaUpdate/<int:pk>/', ProductosMayoristaUpdate.as_view(), name="productosMayoristaUpdate"),
    path('productosMayoristaDelete/<int:pk>/', ProductosMayoristaDelete.as_view(), name="productosMayoristaDelete"), 
    
#___proveedorMercaderia app TiendaPipi by Mica Lira
    path('proveedorMercaderia/', proveedorMercaderia, name="proveedorMercaderia"),
    path('proveedorMercaderiaForm/', proveedorMercaderiaForm, name="proveedorMercaderiaForm"), 
    path('buscarProveedorMercaderia/', buscarProveedorMercaderia, name="buscarProveedorMercaderia"),
    path('encontrarProveedorMercaderia/', encontrarProveedorMercaderia, name="encontrarProveedorMercaderia"),
    path('proveedorMercaderiaUpdate/<id_proveedorMercaderia>/', proveedorMercaderiaUpdate, name="proveedorMercaderiaUpdate"),
    path('proveedorMercaderiaDelete/<id_proveedorMercaderia>/', proveedorMercaderiaDelete, name="proveedorMercaderiaDelete"),

#___EmpresaEnvioClientes app TiendaPipi by Mica Lira
    path('empresaEnvioClientes/', EmpresaEnvioClientesList.as_view(), name="empresaEnvioClientes"),
    path('empresaEnvioClientesCreate/', EmpresaEnvioClientesCreate.as_view(), name="empresaEnvioClientesCreate"),
    path('empresaEnvioClientesUpdate/<int:pk>/', EmpresaEnvioClientesUpdate.as_view(), name="empresaEnvioClientesUpdate"),
    path('empresaEnvioClientesDelete/<int:pk>/', EmpresaEnvioClientesDelete.as_view(), name="empresaEnvioClientesDelete"),
    
#___EntregableProducto app TiendaPipi by Mica Lira
    path('entregableProducto/', EntregableProductoList.as_view(), name="entregableProducto"),
    path('entregableProductoCreate/', EntregableProductoCreate.as_view(), name="entregableProductoCreate"),
    path('entregableProductoUpdate/<int:pk>/', EntregableProductoUpdate.as_view(), name="entregableProductoUpdate"),
    path('entregableProductoDelete/<int:pk>/', EntregableProductoDelete.as_view(), name="entregableProductoDelete"),    


#___LOGIN / LOGOUT / REGISTRACION app TiendaPipi by Mica Lira
    path('login/', loginRequest, name="login"),
    path('logout/', LogoutView.as_view(template_name="tiendapipi/logout.html"), name="logout"),
    path('registro/', register , name="registro"),
    
#______Edicion y avatar - App TiendaPipi
    path('perfil/', editProfile, name="perfil"),
    path('<int:pk>/password', CambiarClave.as_view, name="cambiarClave"),
    path('agregar_avatar/', agregarAvatar, name='agregar_avatar'), 


]
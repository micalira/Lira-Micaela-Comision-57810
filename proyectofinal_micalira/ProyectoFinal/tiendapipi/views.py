# Import Tienda Pipi by Mica Lira

from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse_lazy
from .models import *
from .forms import *

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView, PasswordChangeView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Tienda Pipi by Mica Lira

@login_required
def home(request):
    return render(request, "tiendapipi/home.html")

@login_required
def acerca(request):
    return render(request, "tiendapipi/acerca.html")

#__ ProveedorMercaderia app tiendapipi by Mica Lira

@login_required
def proveedorMercaderia(request):
    contexto = {"ProveedorMercaderia": ProveedorMercaderia.objects.all()}
    return render(request, "tiendapipi/proveedorMercaderia.html",contexto)

@login_required
def proveedorMercaderiaForm(request):
    if request.method == "POST":
        miForm = ProveedorMercaderiaForm(request.POST)
        if miForm.is_valid():
            proveedorMercaderia_nombre = miForm.cleaned_data.get("nombre")
            proveedorMercaderia_pagina = miForm.cleaned_data.get("pagina")
            proveedorMercaderia_email = miForm.cleaned_data.get("email")
            proveedorMercaderia_costoenvio = miForm.cleaned_data.get("costoenvio")
            proveedorMercaderia_demoraenvio = miForm.cleaned_data.get("demoraenvio")
            proveedorMercaderia = ProveedorMercaderia(nombre=proveedorMercaderia_nombre,pagina=proveedorMercaderia_pagina,email=proveedorMercaderia_email,costoenvio=proveedorMercaderia_costoenvio,demoraenvio=proveedorMercaderia_demoraenvio)
            proveedorMercaderia.save()
            contexto = {"proveedorMercaderia": ProveedorMercaderia.objects.all()}
            return render(request, "tiendapipi/proveedorMercaderia.html", contexto)
    else:
        miForm = ProveedorMercaderiaForm()
        
    return render(request, "tiendapipi/proveedorMercaderiaForm.html", {"form": miForm})

@login_required
def buscarProveedorMercaderia(request):
    return render(request,"tiendapipi/buscar.html")

@login_required
def encontrarProveedorMercaderia(request):
    if request.GET["buscar"]:
        patron = request.GET-["buscar"]
        proveedorMercaderia = ProveedorMercaderia.objects.filter(nombre_icontains=patron)
        contexto = {'proveedorMercaderia' : proveedorMercaderia}
    else:
        contexto = {"proveedorMercaderia": ProveedorMercaderia.objects.all()}

    return render(request, "tiendapipi/proveedorMercaderia.html", contexto)

@login_required
def proveedorMercaderiaUpdate(request, id_proveedorMercaderia):
    proveedorMercaderia = ProveedorMercaderia.objects.get(id=id_proveedorMercaderia)
    if request.method == "POST":
        miForm = ProveedorMercaderiaForm(request.POST)
        if miForm.is_valid():
            proveedorMercaderia.nombre = miForm.cleaned_data.get("nombre")
            proveedorMercaderia.pagina = miForm.cleaned_data.get("pagina")
            proveedorMercaderia.email = miForm.cleaned_data.get("email")
            proveedorMercaderia.costoenvio = miForm.cleaned_data.get("costoenvio")
            proveedorMercaderia.demoraenvio = miForm.cleaned_data.get("demoraenvio")
            proveedorMercaderia.save()
            contexto = {"proveedorMercaderia": ProveedorMercaderia.objects.all()}
            return render(request, "tiendapipi/proveedorMercaderia.html", contexto)
    else:
        miForm = ProveedorMercaderiaForm(initial={"nombre": proveedorMercaderia.nombre,"pagina":proveedorMercaderia.pagina,"email":proveedorMercaderia.email,"costoenvio":proveedorMercaderia.costoenvio,"demoraenvio":proveedorMercaderia.demoraenvio})
    
    return render (request, "tiendapipi/proveedorMercaderiaForm.html", {"form": miForm})

@login_required
def proveedorMercaderiaDelete(request, id_proveedorMercaderia):
    proveedorMercaderia = ProveedorMercaderia.objects.get(id=id_proveedorMercaderia)
    proveedorMercaderia.delete()
    contexto = {"proveedorMercaderia": ProveedorMercaderia.objects.all() }
    return render(request, "tiendapipi/proveedorMercaderia.html", contexto)

    
#________Venta Minorista >> Tienda y productos - App tiendapipi by Mica Lira

@login_required    
def tiendaMinorista(request):
    contexto = {"tiendaMinorista": TiendaMinorista.objects.all()}
    return render(request, "tiendapipi/tiendaMinorista.html",contexto)

@login_required
def tiendaMinoristaForm(request):
    if request.method == "POST":
        miForm = TiendaMinoristaForm(request.POST)
        if miForm.is_valid():
            tiendaMinorista_nombre = miForm.cleaned_data.get("nombre")
            tiendaMinorista_apellido = miForm.cleaned_data.get("apellido")
            tiendaMinorista_telefono = miForm.cleaned_data.get("telefono")
            tiendaMinorista_dni = miForm.cleaned_data.get("dni")
            tiendaMinorista_email = miForm.cleaned_data.get("email")
            tiendaMinorista =TiendaMinorista(nombre=tiendaMinorista_nombre,apellido=tiendaMinorista_apellido,telefono=tiendaMinorista_telefono,dni=tiendaMinorista_dni,email=tiendaMinorista_email)
            tiendaMinorista.save()
            contexto = {"tiendaMinorista": TiendaMinorista.objects.all()}
            return render(request, "tiendapipi/tiendaMinorista.html", contexto)
    else:
        miForm = TiendaMinoristaForm()
    return render(request, "tiendapipi/tiendaMinoristaForm.html", {"form": miForm})

@login_required
def buscarTiendaMinorista(request):
    return render(request,"tiendapipi/buscar.html")

@login_required
def encontrarTiendaMinorista(request):
    if request.GET["buscar"]:
        patron = request.GET-["buscar"]
        tiendaMinorista = TiendaMayorista.objects.filter(nombre_icontains=patron)
        contexto = {'tiendaMinorista' : tiendaMinorista}
    else:
        contexto = {"tiendaMinorista": TiendaMinorista.objects.all()}

    return render(request, "tiendapipi/tiendaMinorista.html", contexto)

@login_required
def tiendaMinoristaUpdate(request, id_tiendaMinorista):
    tiendaMinorista = TiendaMinorista.objects.get(id=id_tiendaMinorista)
    if request.method == "POST":
        miForm = TiendaMinoristaForm(request.POST)
        if miForm.is_valid():
            tiendaMinorista.nombre = miForm.cleaned_data.get("nombre")
            tiendaMinorista.apellido = miForm.cleaned_data.get("apellido")
            tiendaMinorista.telefono = miForm.cleaned_data.get("telefono")
            tiendaMinorista.dni = miForm.cleaned_data.get("dni")
            tiendaMinorista.email = miForm.cleaned_data.get("email")
            tiendaMinorista.save()
            contexto = {"tiendaMinorista": TiendaMinorista.objects.all() }
            return render(request, "tiendapipi/tiendaMinorista.html", contexto) 
    else:
        miForm = TiendaMinoristaForm(initial={"nombre": tiendaMinorista.nombre,"apellido":tiendaMinorista.apellido,"telefono":tiendaMinorista.telefono,"dni":tiendaMinorista.dni,"email":tiendaMinorista.email})
    return render (request, "tiendapipi/tiendaMinoristaForm.html", {"form": miForm})


@login_required
def tiendaMinoristaDelete(request, id_tiendaMinorista):
    tiendaMinorista = TiendaMinorista.objects.get(id=id_tiendaMinorista)
    tiendaMinorista.delete()
    contexto = {"tiendaMinorista": TiendaMinorista.objects.all() }
    return render(request, "tiendapipi/tiendaMinorista.html", contexto)

    
#______  

class ProductosMinoristaList(LoginRequiredMixin, ListView):
    model = ProductosMinorista    
    
class ProductosMinoristaCreate(LoginRequiredMixin, CreateView):
    model = ProductosMinorista
    fields = ["nombre","valor","cantidad","tamaño","peso"]
    success_url = reverse_lazy ("productosMinorista")
    
class ProductosMinoristaUpdate(LoginRequiredMixin, UpdateView):
    model = ProductosMinorista
    fields = ["nombre","valor","cantidad","tamaño","peso"]
    success_url = reverse_lazy ("productosMinorista")  
    
class ProductosMinoristaDelete(LoginRequiredMixin, DeleteView):
    model = ProductosMinorista
    success_url = reverse_lazy ("productosMinorista") 
    
#________VENTA POR MAYOR >> Tienda y productos - App tiendapipi by Mica Lira

class TiendaMayoristaList(LoginRequiredMixin, ListView):
    model = TiendaMayorista

class TiendaMayoristaCreate(LoginRequiredMixin, CreateView):
    model = TiendaMayorista
    fields = ["nombre","apellido","telefono","dni","email"]
    success_url = reverse_lazy ("tiendaMayorista")
    
class TiendaMayoristaUpdate(LoginRequiredMixin, UpdateView):
    model = TiendaMayorista
    fields = ["nombre","apellido","telefono","dni","email"]
    success_url = reverse_lazy ("tiendaMayorista")  
    
class TiendaMayoristaDelete(LoginRequiredMixin, DeleteView):
    model = TiendaMayorista
    success_url = reverse_lazy ("tiendaMayorista") 

#____________       

class ProductosMayoristaList(LoginRequiredMixin, ListView):
    model = ProductosMayorista

class ProductosMayoristaCreate(LoginRequiredMixin, CreateView):
    model = ProductosMayorista
    fields = ["nombre","valor","cantidad","tamaño","peso"]
    success_url = reverse_lazy ("productosMayorista")
    
class ProductosMayoristaUpdate(LoginRequiredMixin, UpdateView):
    model = ProductosMayorista
    fields = ["nombre","valor","cantidad","tamaño","peso"]
    success_url = reverse_lazy ("productosMayorista")  
    
class ProductosMayoristaDelete(LoginRequiredMixin, DeleteView):
    model = ProductosMayorista
    success_url = reverse_lazy ("productosMayorista")    
    
    
#________Envios de productos - App tiendapipi by Mica Lira    

class EmpresaEnvioClientesList(LoginRequiredMixin, ListView):
    model = EmpresaEnvioClientes

class EmpresaEnvioClientesCreate(LoginRequiredMixin, CreateView):
    model = EmpresaEnvioClientes
    fields = ["nombre","pagina","email","costoenvio","demoraenvio"]
    success_url = reverse_lazy ("empresaEnvioClientes")
    
class EmpresaEnvioClientesUpdate(LoginRequiredMixin, UpdateView):
    model = EmpresaEnvioClientes
    fields = ["nombre","pagina","email","costoenvio","demoraenvio"]
    success_url = reverse_lazy ("empresaEnvioClientes")  
    
class EmpresaEnvioClientesDelete(LoginRequiredMixin, DeleteView):
    model = EmpresaEnvioClientes
    success_url = reverse_lazy ("empresaEnvioClientes") 

#____________   

class EntregableProductoList(LoginRequiredMixin, ListView):
    model = EntregableProducto

class EntregableProductoCreate(LoginRequiredMixin, CreateView):
    model = EntregableProducto
    fields = ["nombre","provincia","empresaenvio","fechaEntrega","entregado"]
    success_url = reverse_lazy ("entregableProducto")
    
class EntregableProductoUpdate(LoginRequiredMixin, UpdateView):
    model = EntregableProducto
    fields = ["nombre","provincia","empresaenvio","fechaEntrega","entregado"]
    success_url = reverse_lazy ("entregableProducto")  
    
class EntregableProductoDelete(LoginRequiredMixin, DeleteView):
    model = EntregableProducto
    success_url = reverse_lazy ("entregableProducto")      
    
#______LOGIN / LOGOUT / REGISTRACION TiendaPipi 

def loginRequest (request):
    if request.method == "POST":
        usuarioPipi = request.POST["username"]
        contraseña = request.POST["password"]
        user = authenticate(request, username=usuarioPipi, password=contraseña)
        if user is not None:
            login(request, user)
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar
            return render (request, "tiendapipi/index.html")  
        else: 
            return redirect(reverse_lazy('login'))
    else:
        miForm = AuthenticationForm()
        
    return render(request, "tiendapipi/login.html", {"form":miForm})

def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm is not None:
            ##usuario = miForm.cleaned_data.get('username')
            miForm.save()
            return redirect(reverse_lazy('home'))
    else:
        miForm = RegistroForm()
        
    return render(request, "tiendapipi/registro.html", {"form":miForm})

#______Edicion y avatar - App TiendaPipi

@login_required
def editProfile(request):
    usuarioPipi = request.user
    if request.method == "POST":
        miForm = UserEditForm(request.POST)
        if miForm.is_valid():
            user = User.objects.get(username=usuarioPipi)
            user.email = miForm.cleaned_data.get("email")
            user.first_name = miForm.cleaned_data.get("first_name")
            user.last_name = miForm.cleaned_data.get("last_name")
            user.save()
            return redirect(reverse_lazy ("home"))
    else:
        miForm = UserEditForm(instance=usuarioPipi)
    return render(request, "tiendapipi/editarPerfil.html", {"form":miForm})
            
class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = "tiendapipi/cambiar_clave.html"
    success_url = reverse_lazy("home")
    
@login_required    
def agregarAvatar(request):
    if request.method == "POST":
        print("POST data:", request.POST)
        print("FILES data:", request.FILES)
        miForm = AvatarForm(request.POST, request.FILES)
        if miForm.is_valid():
            usuarioPipi = User.objects.get(username=request.user)
            imagen = miForm.cleaned_data["imagen"]
            avatarViejo = Avatar.objects.filter(user=usuarioPipi)
            if len (avatarViejo) > 0 :
                for i in range (len(avatarViejo)):
                    avatarViejo[i].delete()
            avatar = Avatar(user=usuarioPipi, imagen = imagen)
            avatar.save()
            imagen = Avatar.objects.get(user=usuarioPipi).imagen.url
            request.session["avatar"] = imagen
            
            
            return redirect(reverse_lazy("home"))
    else:
        miForm = AvatarForm()
    return render(request, "tiendapipi/agregarAvatar.html", {"form": miForm})

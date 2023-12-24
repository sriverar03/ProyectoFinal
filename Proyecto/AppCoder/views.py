from django import forms, template
from django.shortcuts import redirect, render
from AppCoder.forms import BlogFormulario,ComentarioFormulario,UserCreationFormulario,UserUpdateFormulario
from . import models
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate,logout





def inicio_view(request):
    blogs = models.Blog.objects.all()    
    return render(request, "AppCoder/inicio.html",{"blogs":blogs})


def login_view1(request):
    return render(request, "AppCoder/login.html")


def login_view(request):
    if request.user.is_authenticated:
        return render(
            request,
            "AppCoder/inicio.html",
            {"mensaje": f"Ya estás autenticado: {request.user.username}"}
        )

    if request.method == "GET":
        return render(
            request,
            "AppCoder/login.html",
            {"form": AuthenticationForm()}
        )
    else:
        formulario = AuthenticationForm(request, data=request.POST)
        blogs = models.Blog.objects.all() 

        if formulario.is_valid():
            informacion = formulario.cleaned_data            
            usuario = informacion["username"]
            password = informacion["password"]

            modelo = authenticate(username=usuario, password=password)
            #print(modelo.id)
            login(request, modelo)
            perfil = models.Avatar.objects.filter(user=modelo)
            
            return render(
                request,
                "AppCoder/inicio.html",
                {"mensaje": f"Bienvenido {modelo.username}","perfil":perfil,"blogs":blogs}
            )
        else:
            return render(
                request,
                "AppCoder/login.html",
                {"form": formulario}
            )


def logout_view(request):
    logout(request)
    return render(request,"Appcoder/logout.html")

def about_view(request):   
    return render(request,"Appcoder/about.html")


def buscar_blog_view (request):
    
    if request.method == 'POST':
        datos = models.Blog.objects.filter(titulo__icontains = request.POST['titulo'])   
        msg = '' if len(datos) > 0 else 'No Existen registro Asociados a la busqueda'
        return render(request, 'AppCoder/buscarBlog.html',{'filtro':datos,'valida':msg}) 
    else:
        return render(request, 'AppCoder/buscarblog.html') 


def detalle_blog_view(request):
    return render(request, 'AppCoder/detalleblog.html')


def ver_blog_view(request,id_blog):
    
    if request.method == 'GET':
        datos = models.Blog.objects.filter(id = id_blog) 
        comentario = models.Comentario.objects.filter(blog_id = id_blog) 
        #msg = '' if len(datos) > 0 else 'No Existen registro Asociados a la busqueda'
        return render(request, 'AppCoder/verblog.html',{'filtro':datos,'comentario':comentario}) 
   
def nuevo_blog_view(request):
    return render(request, "AppCoder/inicio.html")   
    

def crear_blog_view(request):
    msg=''
    if request.method == 'POST':
        form = BlogFormulario(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            msg= "Blog ha sido creado en el Sistema."            
            return render(request, "AppCoder/nuevoblog.html", {'msg': msg,"form": BlogFormulario()})
    else:      
        miformulario = BlogFormulario()
        return render(request, "AppCoder/nuevoblog.html",{"form": miformulario,'msg': msg})


def crear_comentario_view(request):
    msg=''
    if request.method == 'POST':
        form = ComentarioFormulario(request.POST)
        
        if form.is_valid():
            form.save()
            datos = models.Blog.objects.filter(id = request.POST['blog']) 
            comentario = models.Comentario.objects.filter(blog_id = request.POST['blog']) 
            #msg = '' if len(datos) > 0 else 'No Existen registro Asociados a la busqueda'
            return render(request, 'AppCoder/verblog.html',{'filtro':datos,'comentario':comentario})                      
           
    else:      
        miformulario = ComentarioFormulario()
        return render(request, "AppCoder/comentario.html",{"form": miformulario,'msg': msg})


def cargar_blog_view(request,id_blog):
    datos = models.Blog.objects.get(pk = id_blog)
    form = BlogFormulario(request.POST or None,request.FILES or None,instance=datos)
    
    if form.is_valid():
        form.save()
        #msg= "Blog ha sido creado en el Sistema."            
        return render(request, "AppCoder/buscarblog.html")
        
         
    return render(request, 'AppCoder/updateblog.html',{'form':form})

def delete_blog_view(request,id_blog):
     datos = models.Blog.objects.get(pk = id_blog)
     datos.delete()
     return render(request, "AppCoder/buscarblog.html")
     


def crear_perfil_view(request):
    msg=''
    if request.method == 'POST':
        form = UserCreationFormulario(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            msg= "Blog ha sido creado en el Sistema."            
            return render(request, "AppCoder/nuevoperfil.html", {'msg': msg,"form": BlogFormulario()})
    else:      
        miformulario = UserCreationFormulario()
        return render(request, "AppCoder/nuevoperfil.html",{"form": miformulario,'msg': msg})



def cargar_perfil_view(request,id_user):
    blogs = models.Blog.objects.all() 
    datos_user = models.User.objects.get(pk = id_user)    
    form = UserUpdateFormulario(request.POST or None,request.FILES or None,instance=datos_user)
    #print(datos.user.username)
    
    if form.is_valid():        
        form.save()  
        return render(request, "AppCoder/inicio.html",{"blogs":blogs})
        
         
    return render(request, 'AppCoder/updateperfil.html',{'form':form})
    
  
    
    
    

"""
def crear_cliente_view(request):
    msg=''
    if request.method == 'POST':
        form = ClienteFormulario(request.POST)
        if form.is_valid():
            form.save()
            msg= "Cliente " + request.POST['nombre']+ "  "+ request.POST['apellido']+ " ha sido creado en el Sistema."            
            return render(request, "AppCoder/nuevocliente.html", {'msg': msg,"form": ClienteFormulario()})
    else:      
        miformulario = ClienteFormulario()
        return render(request, "AppCoder/nuevocliente.html",{"form": miformulario,'msg': msg})

def buscar_cliente_view (request):
    
    if request.method == 'POST':
        datos = models.Cliente.objects.filter(nombre = request.POST['nombre'])   
        msg = '' if len(datos) > 0 else 'No Existen registro Asociados a la busqueda.'
        return render(request, 'AppCoder/buscarcliente.html',{'filtro':datos,'valida':msg}) 
    else:
        return render(request, 'AppCoder/buscarcliente.html')       
        
        
def paises_view(request):
    return render(request, "AppCoder/nuevopais.html")  


def crear_pais_view(request):
    msg=''
    if request.method == 'POST':
        form = PaisFormulario(request.POST)
        if form.is_valid():
            form.save()
            msg= "País agregado en el Sistema."            
            return render(request, "AppCoder/nuevopais.html", {'msg': msg,"form": PaisFormulario()})
    else:      
        miformulario = PaisFormulario()
        return render(request, "AppCoder/nuevopais.html",{"form": miformulario,'msg': msg})  
    

def buscar_pais_view (request):
    
    if request.method == 'POST':
        datos = models.Paises.objects.filter(nombre = request.POST['nombre'])   
        msg = '' if len(datos) > 0 else 'No Existen registro Asociados a la busqueda'
        return render(request, 'AppCoder/buscarpais.html',{'filtro':datos,'valida':msg}) 
    else:
        return render(request, 'AppCoder/buscarpais.html') 
    
    
def viajes_view(request):
    msg=''
    if request.method == 'POST':
        form = ViajesFormulario(request.POST)
        if form.is_valid():
            form.save()
            msg= "Solicitud de viajes agregada.."            
            return render(request, "AppCoder/solicitudViaje.html", {'msg': msg,"form": ViajesFormulario()})
    else:      
        miformulario = ViajesFormulario()
        return render(request, "AppCoder/solicitudViaje.html",{"form": miformulario,'msg': msg}) 


def buscar_viaje_view (request):
    
    if request.method == 'POST':
        viajes = models.Viajes.objects.filter(Cliente__nombre__contains  = request.POST['nombre']) 
        msg = '' if len(viajes) > 0 else 'No Existen registro Asociados a la busqueda'
        return render(request, 'AppCoder/buscarviajes.html',{'viajes':viajes,'valida':msg}) 
    else:
        return render(request, 'AppCoder/buscarviajes.html') 


def listar_viajes_view (request):
    viajes = models.Viajes.objects.all()    
    return render(request, 'AppCoder/listar_viajes.html', {"viajes": viajes})

def listar_clientes_view (request):
    clientes = models.Cliente.objects.all()    
    return render(request, 'AppCoder/listar_clientes.html', {"clientes": clientes})

def listar_paises_view (request):
    paises = models.Paises.objects.all()    
    return render(request, 'AppCoder/listar_paises.html', {"paises": paises})



"""  
    





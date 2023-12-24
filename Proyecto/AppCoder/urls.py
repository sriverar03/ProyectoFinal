from django.urls import path
from AppCoder.views import about_view,cargar_perfil_view,crear_perfil_view,delete_blog_view,cargar_blog_view,crear_comentario_view,logout_view,login_view, inicio_view,buscar_blog_view,detalle_blog_view,ver_blog_view,nuevo_blog_view,crear_blog_view


urlpatterns = [    
    path("inicio/", inicio_view,name="home"),
    path("login/", login_view, name="login"),
    path("logout/",logout_view, name="logout"),
    path("about/",about_view, name="about"),
    path("Buscarblog/",buscar_blog_view, name="Buscarblog"),
    path("detalleblog/",detalle_blog_view, name="detalleblog"),
    path("verblog/<id_blog>",ver_blog_view, name="verblog"),
    path("nuevoblog/", crear_blog_view,name="nuevoblog"),
    path("comentario/", crear_comentario_view,name="newcomentario"),
    path("updateblog/<id_blog>",cargar_blog_view, name="updateblog"),
    path("deleteblog/<id_blog>",delete_blog_view, name="deleteblog"),
    path("nuevoperfil/", crear_perfil_view,name="nuevoperfil"),
    path("updateperfil/<id_user>",cargar_perfil_view, name="updateperfil"),
    
    
  
]
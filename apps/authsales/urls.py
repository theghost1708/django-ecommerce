from django.urls import path
from apps.authsales import views

urlpatterns = [
    path('signup/', views.signup,name="signup"),
    path('login/', views.handlelogin,name="handlelogin"),
    path('logout/', views.handlelogout,name="handlelogout"),
    path('inicio', views.inicio,name="inicio"),
    path('re', views.re,name="re"),
    path('olvidar', views.olvidar,name="olvidar"),
    path('copy', views.copy,name="copy"),
    path('salir/', views.salir,name="salir"),

    path('opciones', views.opciones,name="menu-opciones/opciones"),
    path('pollo', views.pollo,name="menu-opciones/pollo"),
    path('vaca', views.vaca,name="menu-opciones/vaca"),
    path('cerdo', views.cerdo,name="menu-opciones/cerdo"),
    path('copy2', views.copy2,name="menu-opciones/copy2"),
    path('cat', views.cat,name="menu-opciones/cat"),
    path('dog', views.dog,name="menu-opciones/dog"),
    path('parrot', views.parrot,name="menu-opciones/parrot"),
    path('java_parrot', views.java_parrot,name="menu-opciones/java_parrot"),
    path('rata', views.rata,name="menu-opciones/rata"),
    path('ferret', views.ferret,name="menu-opciones/ferret"),
]

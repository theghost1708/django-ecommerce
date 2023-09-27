from django.urls import path
from apps.products import views

urlpatterns = [
    path('', views.index,name="menu-inicio/index"),
    path('inicio', views.inicio,name="menu-inicio/inicio"),
    path('re', views.re,name="menu-inicio/re"),
    path('olvidar', views.olvidar,name="menu-inicio/olvidar"),
    path('copy', views.copy,name="menu-inicio/copy"),
    
    
]
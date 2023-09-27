from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
def signup(request):
    
    if(request.method=="POST"):
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['passwd1']
        con_password = request.POST['passwd2']

        if(password != con_password):
            messages.warning(request, "Password incorrect!")
            return render(request, "authentication/signup.html")
        try:
            if(User.objects.get(username = email)):
                messages.warning(request, "User already exist!")
                return render(request, "authentication/signup.html")
        except Exception as identifier:
            pass
        user = User.objects.create_user(email, email, password)
        user.save()
        messages.warning(request, "User created!")
        return render(request, "authentication/signup.html")
    return render(request, "authentication/signup.html")

@login_required
def handlelogin(request):
    return render(request, "authentication/login.html")

def salir(request):
    logout(request)
    return redirect('/')

def handlelogout(request):
    return redirect('/auth/login')

def index(request):
    return render(request, "menu-inicio/index.html")

def inicio(request):
    return render(request, "authentication/inicio.html")

def re(request):
    return render(request, "authentication/re.html")

def olvidar(request):
    return render(request, "authentication/olvidar.html")

def copy(request):
    return render(request, "authentication/copy.html")

def opciones(request):
    return render(request, "menu-opciones/opciones.html")

def pollo(request):
    return render(request, "menu-opciones/pollo.html")

def vaca(request):
    return render(request, "menu-opciones/vaca.html")

def cerdo(request):
    return render(request, "menu-opciones/cerdo.html")

def copy2(request):
    return render(request, "menu-opciones/copy2.html")

def cat(request):
    return render(request, "menu-opciones/cat.html")

def dog(request):
    return render(request, "menu-opciones/dog.html")

def parrot(request):
    return render(request, "menu-opciones/parrot.html")

def java_parrot(request):
    return render(request, "menu-opciones/java_parrot.html")

def rata(request):
    return render(request, "menu-opciones/rata.html")

def ferret(request):
    return render(request, "menu-opciones/ferret.html")
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "menu-inicio/index.html")

def inicio(request):
    return render(request, "menu-inicio/inicio.html")

def re(request):
    return render(request, "menu-inicio/re.html")

def olvidar(request):
    return render(request, "menu-inicio/olvidar.html")

def copy(request):
    return render(request, "menu-inicio/copy.html")


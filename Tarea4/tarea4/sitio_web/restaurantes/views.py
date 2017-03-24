from django.shortcuts import render, HttpResponse
from .models import restaurants
# Create your views here.

def index(request):
    context = {}
    return render(request,'index.html',context)

def test(request):
    context = {} #Aqui van las variables para la plantilla
    return render(request,'test.html',context)

def listar(request):
     context = {
        "resta": restaurants.objects[:5], # los cinco primeros
     }
     return render (request, 'restaurantes/listar.html', context)

def buscar(request):
    cocina = request.GET.get('cocina')
    lista = restaurants.objects(cuisine__icontains=cocina)
    context = {
        "resta": lista
    }
    return render(request, 'restaurantes/listar.html', context)

def restaurante(request, id):
    r = restaurants.objects(restaurant_id=id)[0]
    context = {
        "resta": r
    }
    return render (request, 'restaurantes/restaurante.html', context)

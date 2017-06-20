from django.shortcuts import render, HttpResponse
from .models import restaurants
import logging
from django.contrib.auth.decorators import login_required
# Create your views here.

logger = logging.getLogger(__name__)

def index(request):
    logger.info('Una visita más')
    context = {}
    return render(request,'index.html',context)

def archivo(request):
    context = {}
    return render(request,'archivo.html',context)

def texto(request):
    context = {}
    return render(request,'texto.html',context)

def test(request):
    context = {} #Aqui van las variables para la plantilla
    return render(request,'test.html',context)

# def listar(request):
#      context = {
#         "resta": restaurants.objects[:5], # los cinco primeros
#      }
#      return render (request, 'restaurantes/listar.html', context)

# def buscar(request):
#     cocina = request.GET.get('cocina')
#     lista = restaurants.objects(cuisine__icontains=cocina)
#     context = {
#         "resta": lista
#     }
#     return render(request, 'restaurantes/listar.html', context)

@login_required
def restaurante(request, id):
    r = restaurants.objects(restaurant_id=id)[0]
    context = {
        "resta": r
    }
    return render (request, 'restaurantes/restaurante.html', context)

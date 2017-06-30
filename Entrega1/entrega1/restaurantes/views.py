from django.shortcuts import render, HttpResponse, redirect
from .models import restaurants
from .forms import RestaurantForm
import logging
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
# Create your views here.

logger = logging.getLogger(__name__)

def index(request):
    logger.info('Una visita más')
    context = {}
    return render(request,'index.html',context)

def archivo(request):
    context = {        "menu": "imagen"}
    return render(request,'archivo.html',context)

def texto(request):
    context = {        "menu": "texto"}
    return render(request,'texto.html',context)

def test(request):
    context = {} #Aqui van las variables para la plantilla
    return render(request,'test.html',context)

@login_required
def listar(request):
    context = {
        "resta": restaurants.objects[:5],
        "menu": "list"
        } # los cinco primeros
    return render (request, 'restaurantes/listar.html', context)

def buscar(request):
    cocina = request.GET.get('cocina')
    lista = restaurants.objects(cuisine__icontains=cocina)
    context = {
        "resta": lista
    }
    return render(request, 'restaurantes/listar.html', context)

@login_required
def restaurante(request, id):
    r = restaurants.objects(restaurant_id=id)[0]
    context = {
        "resta": r,
        "photo": str(r.restaurant_id)
    }
    return render (request, 'restaurantes/restaurante.html', context)

@login_required
def add(request):
    if request.method == "POST":
        form = RestaurantForm(request.POST, request.FILES)
        if form.is_valid():
            if len(request.FILES) != 0:
                handle_uploaded_file(restaurants.objects.count() + 1, request.FILES['photo'])
            r = form.save()
            return redirect('listar')
    else:
        form = RestaurantForm();
    # GET o error
    context = {
        'form': form,
        "menu": "add"
    }
    return render(request, 'restaurantes/add.html', context)

def detalles(request):
    r = restaurants.objects(restaurant_id=request.GET.get('id'))[0]
    v = r.borough
    return JsonResponse({'v': v})

def handle_uploaded_file(n, f):
    with open('static/img/restaurantes/' + str(n) + '.jpg', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

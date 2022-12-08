from django.shortcuts import render

# Create your views here.
from .models import Películas,Directores

def Director(request):
    Direct = Directores.objects.all()
    return render(request, 'Director.html', {
        'Direct': Direct
    })

def Película (request):
    Pelis = Películas.objects.all()
    return render(request, 'Película.html', {
        'Pelis': Pelis
    })


def index (request):
    num_Peliculas = Películas.objects.all().count()
    num_Directores = Directores.objects.all().count()

    return render(
        request,
        'index.html',
        context={
            'num_Peliculas': num_Peliculas,
            'num_Directores': num_Directores

        }
    )
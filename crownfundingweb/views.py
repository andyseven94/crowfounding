from django.shortcuts import render
from crownfundingweb.models import Categoria, Campania


def home(request):
    categorias = Categoria.objects.all()
    campanias = Campania.objects.all()
    #categorias_campania = campaniaCategorias.Objects.filter()
    return render (request,'index.html', {'lista_categorias':categorias, 'lista_campanias':campanias})
    
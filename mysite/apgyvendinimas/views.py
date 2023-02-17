from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Objektas
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    num_objektas = Objektas.objects.all().count()

    context = {
        'num_objektas': num_objektas,}
    return render(request, 'index.html', context=context)

def skelbimai(request):
    paginator = Paginator(Objektas.objects.all(), 4)
    page_number= request.GET.get("page")
    paged_skelbimai = paginator.get_page(page_number)
    context = {
        'skelbimai' : paged_skelbimai
    }
    return render(request, 'skelbimai.html', context=context)

def skelbimas(request, skelbimas_id):
    skelbimas = get_object_or_404(Objektas, pk = skelbimas_id)
    context = {
        'skelbimas': skelbimas
    }
    return render(request, 'skelbimas.html', context=context)



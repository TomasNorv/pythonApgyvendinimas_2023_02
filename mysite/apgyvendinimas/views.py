from django.shortcuts import render
from django.http import HttpResponse
from .models import Objektas

# Create your views here.

def index(request):
    num_objektas = Objektas.objects.all().count()

    context = {
        'num_objektas': num_objektas,}
    return render(request, 'index.html', context=context)

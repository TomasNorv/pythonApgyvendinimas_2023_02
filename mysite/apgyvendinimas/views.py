from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Objektas
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.

def index(request):
    num_objektas = Objektas.objects.all().count()

    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1
    context = {
        'num_objektas': num_objektas,
        'num_visits': num_visits,
    }
    return render(request, 'index.html', context=context)

def skelbimai(request):
    paginator = Paginator(Objektas.objects.all(), 6)
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


def search(request):
    query = request.GET.get('query')
    print(query)
    search_results = Objektas.objects.filter(Q(city__icontains=query) | Q(type__icontains=query))
    return render(request, 'search.html', {'skelbimai': search_results, 'query': query})


class UserObjektasListView(LoginRequiredMixin, ListView):
    model = Objektas
    template_name = 'user_skelbimai.html'
    paginate_by = 4
    context_object_name = 'skelbimai'

    def get_queryset(self):
        return Objektas.objects.filter(user=self.request.user)


@csrf_protect
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Vartotojo vardas {username} užimtas!')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'Vartotojas su el. paštu {email} jau užregistruotas!')
                    return redirect('register')
                else:
                    User.objects.create_user(username=username, email=email, password=password)
                    messages.info(request, f'Vartotojas {username} užregistruotas!')
                    return redirect('login')
        else:
            messages.error(request, 'Slaptažodžiai nesutampa!')
            return redirect('register')
    return render(request, 'register.html')
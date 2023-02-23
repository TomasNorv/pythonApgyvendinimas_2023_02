from django.shortcuts import render,redirect, reverse, get_object_or_404
from django.http import HttpResponse
from .models import Objektas
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic.edit import FormMixin
from .forms import ObjektasReviewForm, UserUpdateForm, ProfilisUpdateForm
from django.contrib.auth.decorators import login_required

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


class ObjektasDetailView(FormMixin, DetailView):
    model = Objektas
    template_name = 'skelbimas.html'
    context_object_name = 'skelbimas'
    form_class = ObjektasReviewForm
    def get_success_url(self):
        return reverse('skelbimas', kwargs={'pk': self.object.id})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.objektas = self.object
        form.instance.reviewer = self.request.user
        form.save()
        return super(ObjektasDetailView, self).form_valid(form)


class UserObjektasCreateView(LoginRequiredMixin, CreateView):
    model = Objektas
    fields = ['caption', 'type', 'city', 'address', 'street', 'housenumber', 'area', 'phone_nr', 'rooms', 'max_guest', 'price', 'description', 'amenities']
    template_name = 'user_skelbimas_form.html'
    def get_success_url(self):
        return reverse('user_skelbimai')
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)
class UserObjektasUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Objektas
    fields = ['caption', 'type', 'city', 'address', 'street', 'housenumber', 'area', 'phone_nr', 'rooms', 'max_guest',
              'price', 'description', 'amenities']
    template_name = 'user_skelbimas_form.html'
    def get_success_url(self):
        return reverse('user_skelbimai')
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

    def test_func(self):
        objektas = self.get_object()
        return self.request.user == objektas.user



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


@login_required
def profilis(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfilisUpdateForm(request.POST, request.FILES, instance=request.user.profilis)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Profilis atnaujintas")
            return redirect('profilis')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfilisUpdateForm(instance=request.user.profilis)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'profilis.html', context)
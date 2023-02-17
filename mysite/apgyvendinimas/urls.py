from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('skelbimai/', views.skelbimai, name= "visi_skelbimai"),
    path('skelbimai/<int:skelbimo_id>', views.skelbimas, name= 'skelbimas'),


]

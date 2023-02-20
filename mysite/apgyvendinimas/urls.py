from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('skelbimai/', views.skelbimai, name= "visi_skelbimai"),
    path('skelbimai/<int:skelbimas_id>', views.skelbimas, name= 'skelbimas'),
    path('search/', views.search, name='search'),
    path('userskelbimai/', views.UserObjektasListView.as_view(), name="user_skelbimai"),

]

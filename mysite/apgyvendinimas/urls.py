from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('skelbimai/', views.skelbimai, name= "visi_skelbimai"),
    path("skelbimai/<int:pk>", views.ObjektasDetailView.as_view(), name ="skelbimas"),
    path('search/', views.search, name='search'),
    path('userskelbimai/', views.UserObjektasListView.as_view(), name="user_skelbimai"),
    path('register/', views.register, name='register'),
    path('profilis/', views.profilis, name='profilis'),
    path("userskelbimai/create", views.UserObjektasCreateView.as_view(), name ="user_skelbimas_create"),

]

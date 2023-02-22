from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('skelbimai/', views.skelbimai, name= "visi_skelbimai"),
    path('skelbimai/<int:skelbimas_id>', views.skelbimas, name= 'skelbimas'),
    path("skelbimai/<int:pk>", views.ObjektasDetailView.as_view(), name ="skelbimas"),
    path('search/', views.search, name='search'),
    path('userskelbimai/', views.UserObjektasListView.as_view(), name="user_skelbimai"),
    path('register/', views.register, name='register'),
    path('profilis/', views.profilis, name='profilis'),

]

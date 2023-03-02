from django.urls import path, include
from . import views


urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('', views.index, name='index'),
    path('skelbimai/', views.skelbimai, name= "visi_skelbimai"),
    path("skelbimai/<int:pk>", views.ObjektasDetailView.as_view(), name ="skelbimas"),
    path('search/', views.search, name='search'),
    path('userskelbimai/', views.UserObjektasListView.as_view(), name="user_skelbimai"),
    path('register/', views.register, name='register'),
    path('profilis/', views.profilis, name='profilis'),
    path("userskelbimai/create", views.UserObjektasCreateView.as_view(), name ="user_skelbimas_create"),
    path('userskelbimai/<int:pk>/update', views.UserObjektasUpdateView.as_view(), name='user_skelbimas_update'),
    path('userskelbimai/<int:pk>/delete', views.UserObjektasDeleteView.as_view(), name='user_skelbimas_delete'),

]

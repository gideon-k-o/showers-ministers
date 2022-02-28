from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('chats/', views.chats, name='chats'),
    path('history/', views.about, name='about'),
    path('login/', views.login, name='login')
]
 
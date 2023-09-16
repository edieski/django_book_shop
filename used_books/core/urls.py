from django.urls import path
from . import views
from django.contrib.auth import views as auth_views 
from .forms import LoginFormm

app_name = 'core'

urlpatterns = [
    path('home', views.index, name='index'), 
    path('contact/', views.contact, name = 'contact') , 
    path('signup/', views.signup, name= 'signup'), 
    path('login/',auth_views.LoginView.as_view(authentication_form = LoginFormm, template_name = 'core/login.html'), name = 'login' )
]
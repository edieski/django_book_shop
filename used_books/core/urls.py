from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('home', views.index, name='index'), 
    path('contact/', views.contact, name = 'contact') , 
    path('signup/', views.signup, name= 'signup')
]
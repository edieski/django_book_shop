from django.urls import path
from . import views

app_name = 'items'

urlpatterns = [
    path('', views.items, name='items'),
    path('new/', views.new,  name = 'new'),
    path('<pk>/', views.detail, name='detail')
]
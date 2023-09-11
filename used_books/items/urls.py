from django.urls import path
from . import views

app_name = 'items'

urlpatterns = [
    path('<pk>/', views.detail, name='detail')
]
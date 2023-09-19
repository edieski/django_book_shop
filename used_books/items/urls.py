from django.urls import path
from . import views

app_name = 'items'

urlpatterns = [
    path('new/', views.new,  name = 'new'),
    path('<pk>/', views.detail, name='detail'),
    path('<item_id>/delete/', views.delete, name='delete'),
    path('<pk>/edit/', views.edit, name='edit'),
]
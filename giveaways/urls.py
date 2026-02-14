from django.urls import path
from . import views

app_name = 'giveaways'

urlpatterns = [
    path('', views.gift_list, name='gift_list'),
    path('gift/<int:pk>/', views.gift_detail, name='gift_detail'),
    path('gift/<int:pk>/register/', views.register, name='register'),
    path('success/', views.success, name='success'),
]

from django.urls import path
from .import views

urlpatterns = [
    path('', views.view_users, name='View All Users'),
    path('create/', views.add_users, name='Create New User'),
]
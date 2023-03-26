from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.add_client, name='Create New Clients'),
    path(':<int:id>/', views.view_clientById, name='View Client By Id'),
    path(':<int:id>/projects', views.add_projects, name='Add New Project'),
    path('', views.view_clients, name='View All Clients'),
    path(':<int:id>/delete', views.delete, name="Delete All The Data"),
    path(':<int:id>/update', views.update, name="Update Data"),
]
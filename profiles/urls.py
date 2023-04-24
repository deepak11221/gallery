from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.add_profile, name='add_profile'),
    path('view_profile/<int:id>/', views.view_profile, name='view_profile'),
    path('edit_profile/<int:id>/edit/', views.edit_profile, name='edit_profile'),
    path('delete_profile/<int:id>/delete/', views.delete_profile, name='delete_profile'),
    
]
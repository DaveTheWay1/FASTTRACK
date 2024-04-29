from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/logout/', views.user_logout, name='user_logout'),
    path('accounts/signup/', views.signup, name='signup'),
    path('user/<int:user_id>/add_current_balance/', views.add_current_balance, name='add_current_balance'),
]
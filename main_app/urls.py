from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/logout/', views.user_logout, name='user_logout'),
    path('accounts/signup/', views.signup, name='signup'),
]
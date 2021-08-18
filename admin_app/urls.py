from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin_signup', views.admin_signup, name='admin_signup'),
    path('admin_login', views.admin_login, name='admin_login'),
    path('dashboard', views.dashboard, name='dashboard')
]

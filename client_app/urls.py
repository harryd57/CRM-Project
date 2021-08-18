from django.urls import path
from . import views

urlpatterns = [
    path('client_login', views.client_login, name="client_login"),
    path('client_signup', views.client_signup, name="client_signup")
]

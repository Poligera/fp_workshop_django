from django.contrib.auth import views
from django.urls import path

from .views import register

urlpatterns = [
    path("register/", register),

    path('login/', views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='users/logout.html'), name='logout')
]

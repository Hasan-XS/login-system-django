from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register_system, login_sys, welcome_view

urlpatterns = [
    path('', register_system, name="register_sys"),
    path("login/", login_sys, name="login_sys"),
    path("welcome/", welcome_view, name="welcome"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

]

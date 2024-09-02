from django.urls import path,include
from . import views

urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("", views.home_view, name="home"),
    path("mainpage/",include("mainpage.urls"), name="mainpage"),
]

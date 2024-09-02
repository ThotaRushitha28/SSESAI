from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser


def home_view(request):
    return render(request, "login.html")


def register_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        full_name = request.POST["full_name"]
        password = request.POST["password1"]
        confirm_password = request.POST["password2"]

        if password == confirm_password:
            user = CustomUser.objects.create_user(
                email=email, full_name=full_name, password=password
            )
            user.save()
            return redirect("login")
        else:
            error_message = "Passwords do not match. Please try again."
            return render(request, "register.html", {"error_message": error_message})
    return render(request, "register.html")


def login_view(request):
    if request.method == "POST":
        email = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            print('hello')
            return redirect("mainpage")  # Redirect to a home page after login
        else:
            # Return an 'invalid login' error message
            error_message = "Invalid email or password. Please try again."
            return render(request, "login.html", {"error_message": error_message})
    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("login")

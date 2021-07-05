from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from pages.views import index
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.


def register_user(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration Successful.")
            return redirect(index)
        messages.error(
            request, "Unsuccessful Registration. Invalid Information Provided. ")
    else:
        form = NewUserForm()
    return render(request, 'registration/register.html', {"form": form})


def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(
                    request, f"You are now logged in as {username}.")
                return redirect(index)
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, 'registration/login.html', {"form": form})


def logout_user(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    # return redirect("index")
    return render(request, index)

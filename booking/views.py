from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return render(request, "booking/index.html")


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "booking/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try: 
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "booking/regiseter.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return redirect(reverse("index"))
    return render(request, "booking/register.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check in authentication successful
        if user is not None:
            return redirect(reverse("index"))
        else:
            return rnder(request, "booking/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "booking/login.html")
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse

from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.urls import reverse

import json

from .models import *


def index(request):
    popular = Listing.objects.all()

    return render(request, "booking/index.html", {
        "listings": popular[:4]
    })


def catalog(request):
    listings = Listing.objects.all()
    categories = Category.objects.all()
    destinations = Destination.objects.all()

    return render(request, "booking/catalog.html", {
        "listings": listings,
        "categories": categories,
        "destinations": destinations
    })


def catalog_item(request, pk):
    listing = Listing.objects.get(pk=pk)

    return render(request, "booking/catalog_item.html", {
        "listing": listing
    })


@staff_member_required
def create_listing(request):
    pass


def filter(request, location):
    
    location_id = Destination.objects.get(name=location).id
    listings = Listing.objects.filter(location=location_id)

    # Return filtered listings
    return JsonResponse([listing.serialize() for listing in listings], safe=False)


def update_cart(request):
    if request.method != 'POST':
        return JsonResponse({"error": "POST request required."}, status=400)

    # Take JSON string and convert it to dict & get the data needed 
    data = json.loads(request.body)
    listing_id = data.get("id", "")
    action = data.get("action", "")

    print(f"Listing ID: {listing_id} Action: {action}")

    user = request.user
    listing = Listing.objects.get(id=listing_id)
    order, created = Order.objects.get_or_create(user=user, complete=False)
    orderItem, crerated = OrderItem.objects.get_or_create(order=order, listing=listing)

    if action == "add":
        orderItem.quantity += 1
    elif action == "remove":
        orderItem.quantity -= 1

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Cart has been updated.', safe=False)


def cart_view(request):
    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(user=user, complete=False)
        items = order.items.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    return render(request, "booking/cart.html", {
        "items": items,
        "order": order
    })


def checkout(request):
    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(user=user, complete=False)
        items = order.items.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    return render(request, "booking/checkout.html", {
        "items": items,
        "order": order
    })

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
            login(request, user)
            return redirect(reverse("index"))
        else:
            return render(request, "booking/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "booking/login.html")


def logout_view(request):
    logout(request)
    return redirect(reverse("index"))

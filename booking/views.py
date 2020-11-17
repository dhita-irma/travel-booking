from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse

from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.urls import reverse

from datetime import datetime
import json

from . import forms
from .models import *


def index(request):
    """Render homepage"""

    popular = Listing.objects.all()

    return render(request, "booking/index.html", {
        "listings": popular[:4]
    })


def catalog(request):
    """Render page displaying all listings"""

    listings = Listing.objects.all()
    categories = Category.objects.all()
    destinations = Destination.objects.all()

    return render(request, "booking/catalog.html", {
        "listings": listings,
        "categories": categories,
        "destinations": destinations
    })


def catalog_item(request, pk):
    """Render page displaying all listings"""

    # Query for requested listing
    try:
        listing = Listing.objects.get(pk=pk)
    except Listing.DoesNotExist:
        return JsonResponse({"error": f"Listing with pk {pk} not found."}, status=404)

    # Render detail page
    return render(request, "booking/catalog_item.html", {
        "listing": listing
    })


@staff_member_required
def create_listing(request):
    pass


def filter(request, location):
    """API returning filtered listings based on location"""
    
    # Query for requested location
    try:
        location_id = Destination.objects.get(name=location).id
    except Destination.DoesNotExist:
        return JsonResponse({"error": f"Destination '{location}' not found."}, status=404)

    # Return filtered listings
    if request.method == 'GET':
        listings = Listing.objects.filter(location=location_id)
        return JsonResponse([listing.serialize() for listing in listings], safe=False)
    else:
        return JsonResponse({"error": "GET request required."}, status=400)


def update_cart(request):
    """API to update cart items"""

    if request.method != 'POST':
        return JsonResponse({"error": "POST request required."}, status=400)

    # Convert JSON string to dict and get the data needed 
    data = json.loads(request.body)
    listing_id = data.get("id", "")
    action = data.get("action", "")
    date = data.get("date", "")

    print(f"Listing ID: {listing_id} Action: {action}")
    print(f"Reservation date: {date}")

    # Query for order item data
    user = request.user
    listing = Listing.objects.get(id=listing_id)
    reservation_date = datetime.strptime(date, '%b %d, %Y').date()
    order, created = Order.objects.get_or_create(user=user, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, listing=listing, reservation_date=reservation_date)

    # Update quantity based on action
    if action == "add":
        orderItem.quantity += 1
    elif action == "remove":
        orderItem.quantity -= 1
    elif action == "remove_all":
        orderItem.quantity = 0

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse({"message": "Cart updated successfully."}, status=200)


def cart_view(request):
    """Render page displaying items in cart"""

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
    """Render a page to checkout items in cart"""

    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(user=user, complete=False)
        items = order.items.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'pick_up': False}

    return render(request, "booking/checkout.html", {
        "items": items,
        "order": order,
        "contact_form": forms.ContactInfoForm(),
    })


def process_order(request):
    """"API to submit contact information and process payment"""

    if request.method != 'POST':
        return JsonResponse({"error": "POST request required."}, status=400)

    # Convert JSON string to dict
    transaction_id = datetime.now().timestamp()
    data = json.loads(request.body)

    user = request.user
    order, created = Order.objects.get_or_create(user=user, complete=False)

    total = float(data.get("total", ""))
    if total == float(order.get_cart_total):
        order.complete = True
    order.save()

    # Get contact details 
    title = data.get("title", "")
    first_name = data.get("first_name", "")
    last_name = data.get("last_name", "")
    country = data.get("country", "")
    phone_number = data.get("phone_number", "")

    # Save contact details to database
    contact, created = ContactInfo.objects.get_or_create(
        user= request.user,
        title = title,
        first_name = first_name,
        last_name = last_name,
        country = country,
        phone_number = phone_number
    )
    contact.save()

    print("Contact details are saved.")

    return JsonResponse({"message": "Wohoo! Transaction is successful!"}, status=200)


@login_required(login_url='/login/') 
def bookings(request):

    orders = Order.objects.filter(user=request.user, complete=True)
    bookings = []

    # Iterate order items and append it to bookings list
    for order in orders:
        for i in range(order.items.count()):
            bookings.append(order.items.all()[i])

    # Reverse bookings (newest to oldest)
    bookings.reverse()

    return render(request, "booking/bookings.html", {
        "bookings": bookings,
    })
    

@login_required(login_url='/login/') 
def profile(request):
    return render(request, "booking/profile.html", {
        "contact_form": forms.ContactInfoForm()
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

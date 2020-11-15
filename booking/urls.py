from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),

    path("catalog/", views.catalog, name="catalog"),
    path("catalog/<int:pk>", views.catalog_item, name="catalog_item"),
    path("catalog/new/", views.create_listing, name="create"),

    path("cart/", views.cart_view, name="cart"),
    path("checkout/", views.checkout, name="checkout"),

    path("bookings/", views.bookings, name="bookings"),
    # API routes
    path("filter/<str:location>", views.filter, name="filter"),
    path("update_cart/", views.update_cart, name="update_item"),
    path("process_order/", views.process_order, name="process_order")

]
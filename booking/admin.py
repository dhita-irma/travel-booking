from django.contrib import admin

from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "is_staff")


class ListingAdmin(admin.ModelAdmin):
    list_display = ("id", "title")


class DestinationAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ("__str__", "user", "country", "phone_number")


class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "__str__", "user", "complete")

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("id", "__str__", "order", "reservation_date", "quantity")


admin.site.register(User, UserAdmin)
admin.site.register(Listing, ListingAdmin)
admin.site.register(Destination, DestinationAdmin)
admin.site.register(Category)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(ContactInfo, ContactInfoAdmin)


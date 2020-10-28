from django.contrib import admin

from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "is_staff")


class ListingAdmin(admin.ModelAdmin):
    list_display = ("id", "title")


class DestinationAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


admin.site.register(User, UserAdmin)
admin.site.register(Listing, ListingAdmin)
admin.site.register(Destination, DestinationAdmin)
admin.site.register(Category)

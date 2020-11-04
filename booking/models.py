from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    pass


class Destination(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Listing(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=12, decimal_places=0, default=99999)
    location = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name="listings")
    description = models.TextField()
    itinerary = models.TextField()
    category = models.ManyToManyField(Category, blank=True, related_name="listings")
    created_date = models.DateTimeField(default=timezone.now)
    image_url = models.URLField(blank=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title

    def get_categories(self):
        """Return string representation of listing category"""
        categories = ""
        for i in self.category.all():
            categories += i.name + " "
        return categories

    # Return JSON representation of the post
    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "price": self.price,
            "location": self.location.name,
            "description": self.description,
            "itinerary": self.itinerary,
            "category": self.get_categories(),
            "created_date": self.created_date,
            "image_url": self.image_url
        }


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(default=timezone.now)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.transaction_id


class OrderItem(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(default=timezone.now)


class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.address


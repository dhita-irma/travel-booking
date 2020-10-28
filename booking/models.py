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

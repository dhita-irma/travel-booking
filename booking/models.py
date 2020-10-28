from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    pass


class Destination(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Listing(models.Model):
    title = models.CharField(max_length=50)
    location = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name="listings")
    description = models.TextField()
    itinerary = models.TextField()
    category = models.ManyToManyField(Category, blank=True, related_name="listings")
    created_date = models.DateTimeField(default=timezone.now)
    image_url = models.URLField(blank=True)

    def __str__(self):
        return self.title

    
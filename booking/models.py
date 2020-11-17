from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField


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
    created_date = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(blank=True)
    pick_up = models.BooleanField(default=False, null=True, blank=False)
    meeting_point = models.CharField(max_length=200, blank=True, null=True)

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
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        if self.transaction_id == None: 
            return "ERROR: Transaction id is NULL"
        return self.transaction_id

    @property
    def get_cart_total(self):
        all_items = self.items.all()
        total = sum([item.get_total for item in all_items])
        return total

    @property
    def get_cart_items(self):
        all_items = self.items.all()
        total = sum([item.quantity for item in all_items])
        return total

    @property
    def pick_up(self):
        pick_up = False
        orderitems = self.items.all()
        for i in orderitems:
            if i.listing.pick_up == True:
                pick_up = True
        return pick_up

                                                                                                                                                                                                                                                                                                                                                                 
class OrderItem(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True, related_name="items")
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    reservation_date = models.DateField(null=True, blank=True)

    @property
    def get_total(self):
        total = self.listing.price * self.quantity
        return total

    def formatted_date(self):
        return self.reservation_date.strftime('%b %d, %Y')

    def __str__(self):
        return self.listing.title


class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address


class ContactInfo(models.Model):
    TITLE_CHOICES = [
        ('MR', 'MR'),
        ('MRS', 'MRS'),
        ('MISS', 'MISS'),
    ]

    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="contact_info")
    title = models.CharField(max_length=4, choices=TITLE_CHOICES)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    country = CountryField(blank_label='(select country)')
    phone_number = models.CharField(max_length=12) # TODO: Use phone number library

    def __str__(self):
        return f"{self.title} {self.first_name} {self.last_name}"


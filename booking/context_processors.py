from booking.models import Destination, Order


def layout(request):
    destinations = Destination.objects.all()
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(user=request.user, complete=False)
        user = request.user
    else:
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    return {
        'order': order,
        'destinations': destinations,
        }

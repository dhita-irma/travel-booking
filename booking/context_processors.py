from booking.models import Order


def layout(request):
    order, created = Order.objects.get_or_create(user=request.user, complete=False)
    return {'order': order}

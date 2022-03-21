from orders.models import ProductInCart


def getting_cart_info(request):

    session_key = request.session.session_key
    if not session_key:
        #workaround for newer Django versions
        request.session["session_key"] = 123
        #re-apply value
        request.session.cycle_key()

    products_in_cart = ProductInCart.objects.filter(session_key=session_key, is_active=True, order__isnull=True)
    products_total_count = products_in_cart.count()

    return locals()

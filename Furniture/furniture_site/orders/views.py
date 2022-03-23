from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User

from furniture_app.utils import *
from orders.forms import CheckoutContactForm
from orders.models import *


def cart_adding(request):
    return_dict = dict()
    session_key = request.session.session_key
    print(request.POST)
    data = request.POST
    product_id = data.get("product_id")
    count = data.get("count")
    is_delete = data.get("is_delete")

    if is_delete == 'true':
        ProductInCart.objects.filter(id=product_id).update(is_active=False)
    else:
        new_product, created = ProductInCart.objects.get_or_create(session_key=session_key, product_id=product_id,
                                                                     is_active=True, defaults={"count": count})
        if not created:
            print("not created")
            new_product.count += int(count)
            new_product.save(force_update=True)

    #common code for 2 cases
    products_in_cart = ProductInCart.objects.filter(session_key=session_key, is_active=True, order__isnull=True)
    products_total_count = products_in_cart.count()
    return_dict["products_total_count"] = products_total_count

    return_dict["products"] = list()

    for item in products_in_cart:
        product_dict = dict()
        product_dict["id"] = item.id
        product_dict["title"] = item.product.title
        product_dict["price_per_item"] = item.price_per_item
        product_dict["count"] = item.count
        return_dict["products"].append(product_dict)

    return JsonResponse(return_dict)


def checkout(request):
    context = {
        'menu': menu,
        'title': 'Корзина',
    }

    session_key = request.session.session_key
    products_in_cart = ProductInCart.objects.filter(session_key=session_key, is_active=True, order__isnull=True)
    print(products_in_cart)

    form = CheckoutContactForm(request.POST or None)
    if request.POST:
        print(request.POST)
        if form.is_valid():
            print("yes")
            data = request.POST
            name = data.get("name", "3423453")
            phone = data["phone"]
            user, created = User.objects.get_or_create(username=phone, defaults={"first_name": name})

            order = Order.objects.create(user=user, customer_name=name, customer_phone=phone, status_id=1)

            for name, value in data.items():
                if name.startswith("product_in_cart_"):
                    product_in_cart_id = name.split("product_in_cart_")[1]
                    product_in_cart = ProductInCart.objects.get(id=product_in_cart_id)
                    product_in_cart.count = value
                    product_in_cart.order = order
                    product_in_cart.save(force_update=True)

                    ProductInOrder.objects.create(product=product_in_cart.product, count=product_in_cart.count,
                                                  price_per_item=product_in_cart.price_per_item,
                                                  total_price=product_in_cart.total_price,
                                                  order=order)

            return HttpResponseRedirect(request.META['HTTP_REFERER'])
        else:
            print("no")
    return render(request, 'orders/checkout.html', context)

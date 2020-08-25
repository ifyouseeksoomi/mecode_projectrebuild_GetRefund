import json, bcrypt, jwt, random

from django.views import View
from django.http import (
    HttpResponse,
    JsonResponse
)

from user.utils import login_check

from user.models import User
from product.models import (
    Product,
    Applying,
    Color,
    Image,
    ImageCategory
)
from .models import (
    Order,
    OrderStatus
)


class CartItemView(View):
    @login_check
    def post(self, request):
        data = json.loads(request.body)
        if not Order.objects.filter(user_id=request.user.id, product_id = data['product_id'], order_status_id=1).exists():
            Order.objects.create(
                user_id         = request.user.id,
                product_id      = Product.objects.get(id= data['product_id']).id,
                order_status_id = OrderStatus.objects.get(name= 'pending').id,
                quantity        = data['quantity']
            )

            return JsonResponse({'message': 'ITEM_SUCCEESSFULLLY_ADDED'}, status=200)
        return JsonResponse({'message': 'ITEM_ALREADY_EXISTS'}, status=400)

    @login_check
    def get(self, request):
        try:
            cart = Order.objects.filter(user_id=request.user.id, order_status_id=1).select_related('product').prefetch_related('product__image_set')
            cart_list = [{
            'id'             : product.id,
            'product_id'     : product.id,
            'name'           : product.product.name,
            'color'          : product.product.color.name,
            'price'          : product.product.price,
            'product_images' : product.product.image_set.get(image_category_id=1).image_url,
            'quantity'       : product.quantity
            } for product in cart ]
            return JsonResponse({'cart_list' : cart_list })

        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)





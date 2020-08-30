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

            return JsonResponse({'message': 'ITEM_SUCCESSFULLY_ADDED'}, status=200)
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

    @login_check
    def patch(self, request):
        data        = json.loads(request.body)
        cart        = Order.objects.filter(user_id= request.user.id, order_status_id=1).prefetch_related('product')
        cart_item   = cart.get(id=data['cartitem_id'])

        if data['action'] == 'plus': 
            cart_item.quantity +=1
        if data['action'] == 'minus':
            cart_item.quantity -=1
        else:
            JsonResponse ({'message': 'INVALID_ACTION'}, status=400)

        cart_item.save(update_fields=['quantity'])

        cart_list = [{
            'id'                    : product.id,
            'product_id'            : product.product.id,
            'name'                  : product.product.name,
            'color'                 : product.product.color.name,
            'price'                 : product.product.price,
            'product_image'         : product.product.image_set.get(image_category_id=1).image_url,
            'quantity'              : product.quantity
            } for product in cart ]

        return JsonResponse ({'cart_list': cart_list}, status = 200)

    #except KeyError:
    #    JsonResponse ({'message': 'INVALID_ACTION'})

    @login_check
    def delete(self, request):
        data        = json.loads(request.body)
        cart        = Order.objects.filter(user_id = request.user.id, order_status_id=1).prefetch_related('product')
        cart_item   = cart.get(id=data['cartitem_id'])
        cart_item.delete()

        cart_list = [{
            'id'                    : product.id,
            'product_id'            : product.product.id,
            'name'                  : product.product.name,
            'color'                 : product.product.color.name,
            'price'                 : product.product.price,
            'product_image'         : product.product.image_set.get(image_category_id=1).image_url,
            'quantity'              : product.quantity
            } for product in cart ]

        return JsonResponse({'cart_list' : cart_list}, status = 200)

class RecommendationView(View):
    def get(self, request):
        PRODUCT_LIMIT = 18
        product_list = [i for i in Product.objects.all() if i.id < PRODUCT_LIMIT]
        recommend_list = [i for i in random.sample(product_list, 3)]
        data = [{
            'id' : i.id,
            'name' : i.name,
            'color' : i.color.name,
            'price' : i.price,
            'product_image' : i.image_set.get(image_category_id=1).image_url} for i in recommend_list ]

        return JsonResponse ({'data' : data}, status=200)


class QuantityView(View):
    @login_check
    def get(self, request):
        cart = Order.objects.filter(user_id = request.user.id, order_status=1)
        item_quantity_list = [i.quantity for i in cart]
        total_quantity = sum(item_quantity_list)

        return JsonResponse({'total_quantity':total_quantity})











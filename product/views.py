import json
import random
import bcrypt
import jwt

from django.views import View
from django.http  import (
    HttpResponse,
    JsonResponse
)
from django.db.models import Q

from product.models import (
    Product, 
    Category, 
    Applying,
    Color, 
    Image, 
    ImageCategory, 
    DetailInfo
)

class ProductsView(View):
    def get(self, request):
        category_names = request.GET.getlist('category_names')
        applying_names = request.GET.getlist('applying_names')

        q = Q()
        if category_names:
            q &= Q(category__name__in=category_names)
        if applying_names:
            q &= Q(applying__name__in=applying_names)

#        products = Product.objects.prefetch_related('image_set').filter(Q(category__name__in = category_names) & Q(applying__name__in = applying_names))

        products = Product.objects.prefetch_related('image_set').filter(q)

        productlist = [{
            "product_id"    : product.id,
            "product_name"  : product.name,
            "product_group" : product.group,
            "product_image" : product.image_set.get(image_category=1).image_url,
            "model_image"   : product.image_set.get(image_category=2).image_url,
            "product_price" : product.price
        } for product in products ]

        return JsonResponse({'productlist' : productlist}, status=200)

class ProductDetailView(View):
    def get(self, request, product_id):
        PRODUCT_LIMIT = 18
        if product_id < PRODUCT_LIMIT:
            product                        = Product.objects.select_related('color').prefetch_related('image_set').get(id = product_id)
            product_color                  = Product.objects.select_related('color').filter(group= product.group)

            data = {
                'id'                       : product.id,
                'name'                     : product.name,
                'group'                    : product.group,
                'price'                    : product.price,
                'volume'                   : product.volume,
                'description'              : product.description,
                'note'                     : product.note,
                'color'                    : { 'name': product.color.name },
                'color_group'              : [{
                    'product_id'    : i.id,
                    'name'          : i.color.name,
                    'hexcode'       : i.color.hexcode
                } for i in product_color],
                'product_image'            : product.image_set.get(image_category_id=1).image_url,
                'detail_image'             : [ i.image_url for i in product.image_set.filter(image_category_id=3) ]
            }

            return JsonResponse ({'data':data}, status=200)

        else:
            gift_card = Product.objects.prefetch_related('image_set').get(id=product_id)

            data = {
                'id'                       : gift_card.id,
                'name'                     : gift_card.name,
                'group'                    : gift_card.group,
                'price'                    : gift_card.price,
                'volume'                   : gift_card.volume,
                'description'              : gift_card.description,
                'product_image'            : gift_card.image_set.get(image_category_id=1).image_url,
                'detail_image'             : gift_card.image_set.get(image_category_id=3).image_url
            }

            return JsonResponse({'data': data}, status=200)

class PairWithView(View):
    def get(self, request, product_id):
        product_applying_id = Product.objects.get(id=product_id).applying_id
        PRODUCT_LIMIT = 18
        if product_id < PRODUCT_LIMIT:
            pair_product_list   = [ i for i in Product.objects.all() if i.id < PRODUCT_LIMIT]
            pair_product_filter = [ i for i in pair_product_list if i.applying_id != product_applying_id]
            pair_product_final  = [ i for i in random.sample(pair_product_filter, 2)]
            data                = [{
                'id' : i.id,
                'name' : i.name,
                'group' : i.group,
                'price' : i.price,
                'product_image' : i.image_set.get(image_category_id=1).image_url
            } for i in pair_product_final]

            return JsonResponse ({'data': data})

        else:
            return HttpResponse(status=404)

class BelowInfoView(View):
    def get(self, request, product_id):
        try:
            detail_info = DetailInfo.objects.select_related("product").get(id=product_id)

            data = {
                'text1'      : detail_info.text1,
                'message1'   : detail_info.message1,
                'image_url1' : detail_info.image_url1,
                'text2'      : detail_info.text2,
                'message2'   : detail_info.message2,
                'image_url2' : detail_info.image_url2
            }
            
            return JsonResponse({"data" : data})
        
        except DetailInfo.DoesNotExist:
            return HttpResponse(status=404)


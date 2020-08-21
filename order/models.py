from django.db import models

from user.models    import User
from product.models import (
    Product,
    Color,
    Image,
    ImageCategory,
)

class Order(models.Model):
    order_status = models.ForeignKey("OrderStatus", on_delete = models.CASCADE, default = "")
    user         = models.ForeignKey(User, on_delete = models.CASCADE, default = "")
    product      = models.ForeignKey(Product, on_delete = models.CASCADE, default = "")
    quantity     = models.IntegerField(default = 0)
    created_at   = models.DateTimeField(auto_now_add = True)

    class Meta:
        db_table = "orders"


class OrderStatus(models.Model):
    name = models.CharField(max_length=50, default="")

    class Meta:
        db_table = "order_statuses"


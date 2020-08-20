from django.db      import models

class User(models.Model):
    first_name  = models.CharField(max_length=50)
    last_name   = models.CharField(max_length=50)
    birthday    = models.DateField()
    email       = models.EmailField(max_length=200)
    password    = models.CharField(max_length=100)
    item        = models.ManyToManyField('product.Product', through='order.Order', related_name='order_item')
    created_at  = models.DateTimeField(auto_now_add = True)
    updated_at  = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = "users"

    def __str__(self):
        return self.email
    

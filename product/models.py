from django.db import models

class Product(models.Model):
    name        = models.CharField(max_length = 50, default = "")
    group       = models.CharField(max_length = 50, default = "")
    description = models.CharField(max_length = 2000, default = "")
    note        = models.CharField(max_length = 3000, null = True)
    volume      = models.CharField(max_length = 50, default = "")
    price       = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0)
    category    = models.ForeignKey('Category', on_delete = models.CASCADE, default = "")
    applying    = models.ForeignKey('Applying', on_delete = models.CASCADE, default = "")
    color       = models.ForeignKey('Color', on_delete = models.CASCADE, default = "")

    class Meta:
        db_table = 'products'

class Category(models.Model):
    name = models.CharField(max_length=20, default="")

    class Meta:
        db_table = 'categories'

class Applying(models.Model):
    name = models.CharField(max_length=20, default="")

    class Meta:
        db_table = 'applyings'

class Color(models.Model):
    name    = models.CharField(max_length=50, default="")
    hexcode = models.CharField(max_length=20, null=True, default="")

    class Meta:
        db_table = 'colors'

class Image(models.Model):
    image_url       = models.URLField(max_length=1000, default="")
    image_category  = models.ForeignKey('ImageCategory', on_delete=models.CASCADE, default="")
    product         = models.ForeignKey('Product', on_delete=models.CASCADE, default="")

    class Meta:
        db_table = 'images'

class ImageCategory(models.Model):
    name = models.CharField(max_length=50, default="")

    class Meta:
        db_table = 'image_categories'

class DetailInfo(models.Model):
    text1 = models.CharField(max_length=50, default="")
    text2 = models.CharField(max_length=50, default="")
    message1 = models.CharField(max_length=100, default="")
    message2 = models.CharField(max_length=100, default="")
    image_url1 = models.URLField(max_length=1000, default="")
    image_url2 = models.URLField(max_length=1000, default="")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = 'detail_info'


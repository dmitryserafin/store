from django.db import models
class ProductCategory(models.Model):
    name = models.CharField(max_length=256, unique=True)
    description = models.TextField(null=True,blank=True)

class Product(models.Model):
    name = models.CharField(max_length=512)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    quantity = models.PositiveIntegerField (default=0)
    image = models.ImageField(upload_to='products_images')
    category = models.ForeignKey(to=ProductCategory, on_delete=models.PROTECT)



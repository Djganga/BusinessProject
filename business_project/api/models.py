from django.db import models

# Create your models here.
class Product(models.Model):
    category= models.CharField(max_length=25)
    product= models.CharField(max_length=25)
    description = models.CharField(max_length=500)
    quantity = models.DecimalField(decimal_places=2,max_digits=20)
    mrp = models.DecimalField(decimal_places=2,max_digits=20)
    discount = models.DecimalField(decimal_places=2,max_digits=20,default=0)
    final_price = models.DecimalField(decimal_places=2,max_digits=20)

    def __str__(self):
        return self.category + " || " +self.product

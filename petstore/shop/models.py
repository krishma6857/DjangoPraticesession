from django.db import models

# Create your models here.

class Products(models.Model):
    Prod_id = models.IntegerField()
    Prod_name = models.CharField(max_length=20)
    Prod_type = models.CharField(max_length=20)
    Prod_image = models.ImageField(upload_to='images' , default='')

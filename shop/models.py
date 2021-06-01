from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    desc=models.CharField(max_length=300)
    pub_date=models.DateField()
    image=models.ImageField(upload_to='shop/images', default="")
    price=models.IntegerField(default=0)
    category=models.CharField(max_length=50, default="item")
    subcategory=models.CharField(max_length=50, default="")
    offer=models.BooleanField()
    def __str__(self):
     return self.product_name;
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    place=models.CharField(max_length=11)
    subject=models.CharField(max_length=300)
    def __str__(self):
         return self.name;

    

         
   
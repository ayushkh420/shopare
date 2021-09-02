from django.db import models

# Create your models here.
class Grocery(models.Model):
    Store_name = models.CharField(max_length=50)

    def __str__(self):
        return self.Store_name

class ProductGrocery(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    grocery = models.ForeignKey(Grocery, on_delete=models.CASCADE, default=1)
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="images", default="")
    
    def __str__(self):
        return self.product_name
   


class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    desc = models.TextField()

    def __str__(self):
        return self.name +" - "+ self.email

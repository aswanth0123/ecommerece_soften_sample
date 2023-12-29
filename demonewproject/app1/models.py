from django.db import models

# Create your models here.
class register(models.Model):
    name=models.CharField(max_length=15)
    email=models.EmailField()
    dob=models.DateField()
    address=models.CharField(max_length=50)
    username=models.CharField(max_length=10)
    password=models.CharField(max_length=10)

class product(models.Model):
    pid = models.IntegerField(primary_key=True)
    pname=models.CharField(max_length=10)
    price=models.IntegerField()
    quantity=models.IntegerField()
    image=models.FileField()

class Cart(models.Model):
    product_details=models.ForeignKey(product,on_delete=models.CASCADE)
    user_details=models.ForeignKey(register,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)

class bookings(models.Model):
    user_details=models.ForeignKey(register,on_delete=models.CASCADE)
    item_details=models.ForeignKey(product,on_delete=models.CASCADE)
    date=models.DateField()
    quantity=models.IntegerField()
    total_price=models.IntegerField()
    


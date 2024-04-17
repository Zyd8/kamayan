from django.db import models
from django.contrib.auth.models import User

def item_image_path(instance, filename):
    return f'shop_item_images/{instance.user.id}/{filename}'


class SecondHandItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    images = models.ImageField(upload_to=item_image_path)
    description = models.TextField()
    location = models.CharField(max_length=200)
    payment_method = models.CharField(max_length=100)
    pickup_method = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    condition = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class SwapItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    swapfor = models.CharField(max_length=100)
    images = models.ImageField(upload_to=item_image_path)
    description = models.TextField()
    location = models.CharField(max_length=200)
    pickup_method = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    condition = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


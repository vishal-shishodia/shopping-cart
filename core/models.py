from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=250)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    email = models.EmailField()
    address = models.CharField(max_length=150)
    postal_code = models.CharField(max_length=30)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    
    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return self.user.username

    def total_order_cost(self):
        return sum([item.product.price * item.quantity for item in self.consumer.all()])

class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class OrderItem(models.Model):
    consumer = models.ForeignKey(Profile, related_name='consumer', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '{} with id {} by {}'.format(self.product.name,self.id,self.consumer.user.username)

    def get_cost(self):
        return self.product.price * self.quantity
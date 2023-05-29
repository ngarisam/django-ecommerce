from django.db import models
from django.contrib.auth.models import User 
CATEGORY_CHOICE=(
    ('CR','Curd'),
    ('ML','Milk'),
    ('LS','Lassi'),
    ('MS','Milkshake'),
    ('PN','Paneer'),
    ('GH','Ghee'),
    ('CZ','Cheese'),
    ('IC','Ice-cream'),
)
COUNTY_CHOICES=(
    ('Embu','Embu'),
    ('Nairobi','Nairobi'),
    ('Meru','Meru'),
    ('Kiambu','Kiambu'),
)
STATUS_CHOICES=(
    ('pending','pending'),
    ('confirmed','confirmed'),
    ('shipped','shipped'),
    ('canceled', 'canceled'),
)

class Product(models.Model):
    title=models.CharField(max_length=100)
    selling_price=models.FloatField()
    discounted_price=models.FloatField()
    description=models.TextField()
    composition=models.TextField(default='')
    prodapp=models.TextField(default='')
    category=models.CharField(choices=CATEGORY_CHOICE, max_length=2)
    product_image=models.ImageField(upload_to='product')
    def __str__(self):
        return self.title
class Customer(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    locality=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    mobile=models.IntegerField(default=0)
    county=models.CharField(choices=COUNTY_CHOICES, max_length=20)
    def __str__(self):
        return self.name
class Cart(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE, default=1)
    quantity=models.PositiveIntegerField(default=1)
    @property
    def total_cost(self):
        return self.quantity*self.product.discounted_price
class Payment(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    amount=models.FloatField()
    order_id=models.CharField(max_length=50,blank=True, null=True)
    payment_status=models.CharField(max_length=50,blank=True, null=True)
    paid=models.BooleanField(default=False)
class OrderPlaced(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    ordered_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(choices=STATUS_CHOICES,max_length=50, default='pending')
    payment=models.ForeignKey(Payment, on_delete=models.CASCADE)
    @property
    def total_cost():
        return seld.quantity*self.product.discounted_price
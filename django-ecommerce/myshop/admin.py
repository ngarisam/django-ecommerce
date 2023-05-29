from django.contrib import admin
from . models import Product, Customer,Cart,Payment,OrderPlaced
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display=['id','title', 'discounted_price','category','product_image']

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=['id','user', 'locality','county','mobile']
@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display=['id','user','product','quantity']
@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display=['user','amount','order_id']
@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display=['user','customer','product','quantity','ordered_date','status','payment']




from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
from . models import Product, Customer, Cart
from . forms import CustomerRegistrationForm,CustomerProfileForm
from django.db.models import Count,Q
from django.contrib import messages

def home(request):
    return render(request,"myshop/home.html")
def about(request):
    return render(request,"myshop/about.html")
def contact(request):
    return render(request,"myshop/contact.html")
def Category(request):
    return render(request,"myshop/category.html")

class CategoryView(View):
    def get(self,request,val):
        product=Product.objects.filter(category=val)
        title=Product.objects.filter(category=product[0].category).values('title')
        return render(request,"myshop/category.html",locals())
class ProductDetail(View):
    def get(self, request, pk):
        product=Product.objects.get(pk=pk)
        return render(request, "myshop/product-detail.html", locals())
        
class CustomerRegistrationView(View):
    def get(self,request):
        form=CustomerRegistrationForm()
        return render(request,"myshop/customerregistration.html", locals())
    def post(self, request):
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request, "Your registration was susccessful")
        else:
            messages.warning(request, "An error occured during registration")

        return render(request,"myshop/customerregistration.html", locals())
class ProfileView(View):
    def get(self,request):
        form=CustomerProfileForm
        return render(request, 'myshop/profile.html',locals())
        
    def post(self, request):
        form=CustomerProfileForm(request.POST)
        if form.is_valid():
            user=request.user
            name=form.cleaned_data['name']
            locality=form.cleaned_data['locality']
            mobile=form.cleaned_data['mobile']
            county=form.cleaned_data['county']
            reg=Customer(user=user,locality=locality,mobile=mobile,county=county)
            reg.save()  
            messages.success(request, "Successfully saved the data")
        else:
            messages.warning(request, "Unsuccessful, Kindly fill all the fields")
            
        return render(request, 'myshop/profile.html',locals())
def address(request):
    add=Customer.objects.filter(user=request.user)
    return render(request,'myshop/address.html',locals())
class UpdateAddress(View):
    def get(self, request,pk):
        add=Customer.objects.get(pk=pk)
        form=CustomerProfileForm(instance=add)
        return render(request, 'myshop/updateAddress.html',locals())
    def post(self, request,pk):
        form=CustomerProfileForm(request.POST)
        add=Customer.objects.get(pk=pk)
        if form.is_valid():
            add.user=request.user
            add.name=form.cleaned_data['name']
            add.locality=form.cleaned_data['locality']
            add.mobile=form.cleaned_data['mobile']
            add.county=form.cleaned_data['county']
            
            add.save()  
            messages.success(request, "Successfully saved the data")
        else:
            messages.warning(request, "Unsuccessful, Kindly fill all the fields")
            
        return redirect('address')
def add_to_cart(request):
    user=request.user
    prod_id=request.GET.get('prod_id')
    product=Product.objects.get(id=prod_id)
    Cart(user=user,product=product).save()
    return redirect('/cart')
def show_cart(request): 
    user=request.user
    prod_id=request.GET.get('prod_id')
    cart=Cart.objects.filter(user=user)
    amount=0
    for p in cart:
        value=p.quantity*p.product.discounted_price
        amount=amount+value
        totalamount=amount+70
    return render(request,"myshop/addtocart.html", locals())
def plus_cart(request):
    if(request.method=='GET'):
        prod_id=request.GET['prod_id']
        c=Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save()
        user=request.user
        prod_id=request.GET.get('prod_id')
        cart=Cart.objects.filter(user=user)
        amount=0
        for p in cart:
            value=p.quantity*p.product.discounted_price
            amount=amount+value
            totalamount=amount+70
            data={
                'amount':amount,
                'totalamount':totalamount,
                'quantity':p.quantity
            }
            return JsonResponse(data)
def minus_cart(request):
    if(request.method=='GET'):
        prod_id=request.GET['prod_id']
        c=Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity-=1
        if(c.quantity<1):
            c.quantity=1
        c.save()
        
        user=request.user
        prod_id=request.GET.get('prod_id')
        cart=Cart.objects.filter(user=user)
        amount=0
        for p in cart:
            value=p.quantity*p.product.discounted_price
            amount=amount+value
            totalamount=amount+70
            data={
                'amount':amount,
                'totalamount':totalamount,
                'quantity':p.quantity
            }
            return JsonResponse(data)
def remove_cart(request):
    if(request.method=='GET'):
        prod_id=request.GET['prod_id']
        c=Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        
        user=request.user
        prod_id=request.GET.get('prod_id')
        cart=Cart.objects.filter(user=user)
        amount=0
        for p in cart:
            value=p.quantity*p.product.discounted_price
            amount=amount+value
            totalamount=amount+70
            data={
                'amount':amount,
                'totalamount':totalamount,
                'quantity':p.quantity
            }
            return JsonResponse(data)
class Checkout(View):
    def get(self,request):
        user=request.user
        add=Customer.objects.filter(user=user)
        cart_items=Cart.objects.filter(user=user)
        totalamount=0
        for p in cart_items:
            totalamount+=p.quantity*p.product.discounted_price
        return render(request, "myshop/checkout.html", locals())
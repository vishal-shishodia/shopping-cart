from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import *

def List(request):
    products=Product.objects.all()
    return render(request,'list.html',{'products':products})

def AddOrder(request,id):
    consumer = Profile.objects.get(user=request.user)
    product = Product.objects.get(id=id)
    try:
        order = OrderItem.objects.get(consumer=consumer,product=product)
    except ObjectDoesNotExist:
        order = OrderItem.objects.create(consumer=consumer,product=product,quantity=1)
        order.save()
    else:
        order.quantity+=1
        order.save()
    return redirect('list')

def RemoveOrder(request,id):
    product = Product.objects.get(id=id)
    consumer = Profile.objects.get(user=request.user)
    order = OrderItem.objects.get(consumer=consumer,product=product)
    if order.quantity >1:
        order.quantity-=1
        order.save()
        return redirect('cart')
    else:
        order.delete()
    return redirect('list')

def Cart(request):
    consumer = Profile.objects.get(user=request.user)
    items = OrderItem.objects.filter(consumer=consumer)
    return render(request,'cart.html',{'items':items,'consumer':consumer})




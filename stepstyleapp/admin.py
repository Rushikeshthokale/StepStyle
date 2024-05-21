from django.contrib import admin
from .models import Shoe, Cart,BillingDetails,Order


class ShoeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'price', 'category','size','color']
    list_filter = ['name', 'price', 'category','size','color']
    

admin.site.register(Shoe, ShoeAdmin)

class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'uid', 'pid', 'quantity']
    list_filter = ['uid']

admin.site.register(Cart, CartAdmin)

class BillingAdmin(admin.ModelAdmin):
    list_display=['id','country','fname','lname','address','address2','state_country','postal_zip','email_address','phone','on']
    list_filter=['country','fname','lname','address','address2','state_country','postal_zip','email_address','phone','on']

admin.site.register(BillingDetails,BillingAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','orderid','uid','pid','quantity']

admin.site.register(Order,OrderAdmin)

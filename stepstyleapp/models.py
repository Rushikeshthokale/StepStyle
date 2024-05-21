from django.db import models
from django.contrib.auth.models import User

class Shoe(models.Model):
    CATEGORY_CHOICES = [
        ('Men', 'Men'),
        ('Women', 'Women'),
        ('Kids', 'Kids'),
    ]
    SIZE_CHOICES = [
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
    ]
    COLOR_CHOICES =[
        ('Red','Red'),
        ('Green','Green'),
        ('Blue','Blue'),
        ('Purple','Purple'),
        ('Black','Black'),
        ('White','White'),
    ]
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=500)
    price = models.IntegerField(default=0)
    pimage = models.ImageField(upload_to='image', default=0)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='Men')
    size = models.CharField(max_length=10, choices= SIZE_CHOICES,default="Medium")
    color=models.CharField(max_length=20,choices=COLOR_CHOICES,default="Black")

class Cart(models.Model):
    pid = models.ForeignKey(Shoe, on_delete=models.CASCADE, db_column='pid')
    uid = models.ForeignKey(User, on_delete=models.CASCADE, db_column='uid')
    quantity = models.IntegerField(default=1)

class BillingDetails(models.Model):
    COUNTRY_CHOICES = [
        ('India', 'India'),
        ('Algeria', 'Algeria'),
        ('Afghanistan', 'Afghanistan'),
        ('Ghana', 'Ghana'),
        ('Albania', 'Albania'),
        ('Bahrain', 'Bahrain'),
        ('Colombia', 'Colombia'),
        ('Dominican Republic', 'Dominican Republic'),
        ('Bangladesh', 'Bangladesh'),
    ]
    country = models.CharField(max_length=100, choices=COUNTRY_CHOICES, default='India')
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    address2 = models.CharField(max_length=100, blank=True, null=True)
    state_country = models.CharField(max_length=100)
    postal_zip = models.CharField(max_length=20)
    email_address = models.EmailField()
    phone = models.CharField(max_length=20)
    on = models.CharField(max_length=255)
    
class Order(models.Model):
    orderid = models.IntegerField()
    uid = models.ForeignKey(User,on_delete = models.CASCADE, db_column='uid')
    pid = models.ForeignKey(Shoe,on_delete = models.CASCADE, db_column='pid')  
    quantity = models.IntegerField()

class Contact(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=300)
    



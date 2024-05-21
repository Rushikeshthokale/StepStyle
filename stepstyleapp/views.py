from django.shortcuts import render,redirect,HttpResponse
from stepstyleapp.models import Shoe,Cart,BillingDetails,Order,Contact
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q
from django.contrib import messages
import razorpay
import random
from django.core.mail import send_mail

def homepage(request):
    context={}
    data=Shoe.objects.all()
    context['shoes']=data
    return render (request,'index.html',context)

def userlogin(request):
    if request.method=="GET":
        return render(request,'login.html')
    else:
        context={}
        n=request.POST['username']
        p=request.POST['password']
        if n=='' or p=='':
            context['error']="Please enter all the Fields!!!"
            return render(request,'login.html',context)
        else:
             user = authenticate(username=n,password=p)
             if user is not None:
                login(request,user)
                # context['success']="Logged In Successfully!!!"
                messages.success(request,"Successfully Logged In !!!")
                return redirect('/')
             else:
                context['error']="Please provide correct details"
                return render(request,'login.html',context)

def userlogout(request):
    context={}
    context['success']='Logged Out Successfully!!!'
    logout(request)
    return redirect('/')

    
        
# def register(request):
#     if request.method=='GET':
#        return render(request,'register.html')
#     else:
#         context={}
#         n=request.POST['username']
#         e=request.POST.get['email']
#         p=request.POST['password']
#         cp=request.POST['confirmpass']
#         op=request.POST['otp']
        
        
#         if n=='' or e=='' or p==''or cp=='':
#             context['error']="Please enter all the fields!!!!"
#             return render(request,'register.html',context)
#         elif p!=cp:
#             context['error']="Password and Confirm password must be Same"
#             return render(request,'register.html',context)
#         # elif op!=op1:
#         #     context['error']="Incorrect OTP!!!"
#         #     return render(request,'register.html',context)
#         else:
           
#             user=User.objects.create(username=n,email=e)
#             user.set_password(p) #To set encrypted password
#             user.save()
#             context['success']="Registered Successfully!! Please Login"
#             # return render(request,'login.html',context)
#             messages.success(request,"Successfully Logged In !!!")
#             op1=random.randrange(1000,9999)
#             request.session['email']=op1
#             msg_body = 'Order id is:'+str(op1)
#             send_mail(
#             "OTP",
#             msg_body,
#             "rushithokale21@gmail.com",
#             [e],
#             fail_silently=False
#             )
            
#             return redirect('/login')
# def register(request):
#     if request.method == 'GET':
#         return render(request, 'register.html')
#     else:
#         n = request.POST['username']
#         e = request.POST('email')  # Corrected method call
#         p = request.POST['password']
#         cp = request.POST['confirmpass']   
#         if not all([n, e, p, cp]):
#             messages.error(request, "Please enter all the fields!!!")
#             return render(request, 'register.html')
#         elif p != cp:
#             messages.error(request, "Password and Confirm password must be the same")
#             return render(request, 'register.html')
#         # Add code to verify OTP here
#         else:
#             user = User.objects.create_user(username=n, email=e, password=p)
#             # No need to call user.set_password, create_user sets password encrypted
#             user.save()
#             messages.success(request, "Registered Successfully!! Please Login")
            
#             # Generate OTP and send email
#             op1 = random.randrange(1000, 9999)
#             request.session['email'] = e
#             msg_body = 'Your OTP is: ' + str(op1)
#             send_mail(
#                 "OTP",
#                 msg_body,
#                 "rushithokale21@gmail.com",
#                 [e],
#                 fail_silently=False
#             )
            
#             return redirect('/otp') 
def register(request):
    if request.method=='GET':
       return render(request,'register.html')
    else:
        context={}
        n=request.POST['username']
        e=request.POST['email']
        p=request.POST['password']
        cp=request.POST['confirmpass']
        if n=='' or e=='' or p==''or cp=='':
            context['error']="Please enter all the fields!!!!"
            return render(request,'register.html',context)
        elif p!=cp:
            context['error']="Password and Confirm password must be Same"
            return render(request,'register.html',context)
        else:
            user=User.objects.create(username=n,email=e)
            user.set_password(p) #To set encrypted password
            user.save()
            messages.success(request,"Successfully Logged In !!!")
            return redirect('/login')
             # Generate OTP and send email
            # op1 = random.randrange(1000, 9999)
            # request.session['email'] = e
            # msg_body = 'Your OTP is: ' + str(op1)
            # send_mail(
            #     "OTP",
            #     msg_body,
            #     "rushithokale21@gmail.com",
            #     [e],
            #     fail_silently=False
            # )  
            # return redirect('/otp') 
            # context['success']="Registered Successfully!! Please Login"
            # return render(request,'login.html',context)
            



from django.http import HttpResponseNotAllowed

def otpfunction(request):
    if request.method == "POST":
        otp = request.POST.get('otp')
        a = request.session.get('op1')
        if otp == a:
            return redirect('/login')
        else:
            return redirect('/otp')
    elif request.method == "GET":
        # Handle GET requests here
        return render(request, 'otp.html')  # Or any other response for GET requests
    else:
        return HttpResponseNotAllowed(['POST', 'GET'])


    
def shop(request):
    context={}
    data=Shoe.objects.all()
    context['shoes']=data
    return render(request,'shop.html',context)

def searchShoeByType(request,val):
    context={}
    data=Shoe.objects.filter(category=val)
    context['shoes']=data
    return render(request,'shop.html',context)

def searchShoeBySize(request,vall):
    context={}
    data=Shoe.objects.filter(size=vall)
    context['shoes']=data
    return render(request,'shop.html',context)

def searchShoeByColor(request,val3):
    context={}
    data=Shoe.objects.filter(color=val3)
    context['shoes']=data
    return render(request,'shop.html',context)
    
def shop_single(request,pid):
    context={}
    data=Shoe.objects.filter(id=pid)
    if data.exists():
        context['shoe']=data.first()
    context['products']=Shoe.objects.all()
    return render(request,'shop-single.html',context)



def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method=="GET":
        return render(request,'contact.html')
    else:
        f=request.POST['fname']
        l=request.POST['lname']
        e=request.POST['email']
        s=request.POST['subject']
        m=request.POST['message']
        Contact.objects.create(fname=f,lname=l,email=e,subject=s,message=m)
        msg_body = f"Name: {f} {l}\nSubject:{s}\nEmail: {e}\nMessage: {m}"
        send_mail(
            "Thank you for contacting us!!",
            msg_body,
            "rushithokale21@gmail.com",
            [e],
            fail_silently=False,
        )
        messages.success(request,"Thank you for contacting us!!")
        return redirect('/contact')



def addtocart(request,shoeid):
    
    userid=request.user.id
    if userid is None:
        context={}
        context['error']="Please login so as to add the pet in your cart"
        return render(request,'login.html',context)
    else:
        userid=request.user.id
        users=User.objects.filter(id=userid)
        shoes=Shoe.objects.filter(id=shoeid)
        cart=Cart.objects.create(pid=shoes[0],uid=users[0])
        cart.save()
        messages.success(request,"Product added to cart !!!")
        return redirect('/')
    

def showMyCart(request):
    context={}
    userid=request.user.id
    data=Cart.objects.filter(uid=userid)
    context['mycart']=data
    count=len(data)
    total=0   
    for cart in data:
        total+=cart.pid.price * cart.quantity       
    context['cart']=count
    context['total']=total  
    return render(request,'cart.html',context)





def removeCart(request,cartid):
    data=Cart.objects.filter(id=cartid)
    data.delete()
    messages.success(request,"Product removed from your cart!!!")
    return redirect('/cart')

def confirmorder(request):
    context={}
    userid=request.user.id
    data=Cart.objects.filter(uid=userid)
    context['mycart']=data
    count=len(data)
    total=0
    total1=0
    for cart in data:
        total1=cart.pid.price * cart.quantity
        total+=cart.pid.price * cart.quantity
    context['cart']=count
    context['total']=total  
    context['total1']=total1  
    return render(request,'checkout.html',context)

def placeorder(request):
    if request.method == "POST":       
            c = request.POST['country']
            f = request.POST['fname']
            l = request.POST['lname']
            a = request.POST['address']
            a2 = request.POST['address2']  # Use get() to handle optional field
            s = request.POST['state_country']
            p = request.POST['postal_zip']
            e = request.POST['email_address']
            ph = request.POST['phone']
            od = request.POST['on']
            
            BillingDetails.objects.create(country=c, fname=f, lname=l, address=a, address2=a2, state_country=s, postal_zip=p, email_address=e, phone=ph, on=od)
            context={}
            userid=request.user.id
            data=Cart.objects.filter(uid=userid)
            total=0
            for cart in data:
                total +=cart.pid.price * cart.quantity
            client=razorpay.Client(auth=("rzp_test_ZAKvIqIIsGQ3fe","SSfAEiyQrYNk3SciDLWjetRV"))
            data={"amount":total*100,'currency':"INR",'receipt':''}
            payment=client.order.create(data=data)
            print(payment)
            context['data']=payment
            return render(request, 'pay.html',context)       
    else:
        return HttpResponse("This view only accepts POST requests.")

def updateQuantity(request,incr,cid):       
    c = Cart.objects.filter(id=cid)
    if incr == '0':
        c.update(quantity = c[0].quantity-1)
    else:
        c.update(quantity = c[0].quantity+1)
    return redirect('/cart')

def placeeorder(request):
    userid=request.user.id
    user=User.objects.filter(id=userid)
    mycart=Cart.objects.filter(uid=userid)
    ordid=random.randrange(10000,99999)
    for cart in mycart:
        pet=Shoe.objects.filter(id=cart.pid.id)
        ord=Order.objects.create(uid=user[0],pid=pet[0],quantity=cart.quantity,orderid=ordid)
        ord.save()
    mycart.delete()
    
    msg_body = 'Order id is:'+str(ordid)
    custEmail = request.user.email
    send_mail(
    "Order placed successfully!!", #subject
    msg_body, 
    "rushithokale21@gmail.com", #from
    [custEmail],
    fail_silently=False,
    )    

    
    messages.success(request,'order placed successfully')
    return redirect('/thankyou')




def thankyou(request):
    return render(request,'thankyou.html')


def myorders(request):
    context={}
    user=request.user.id
    orderdetails=Order.objects.filter(uid=user)
    # print('profile',orderdetails,user)
    context['data']=orderdetails
    return render(request,'myorders.html',context)






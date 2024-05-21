from django.urls import path
from stepstyleapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('',views.homepage),
    path('login',views.userlogin),
    path('register',views.register),
    path('shop',views.shop),
    path('shopsingle/<pid>',views.shop_single),
    path('about',views.about),
    path('contact',views.contact),
    path('logout',views.userlogout),
    path('addtocart/<shoeid>',views.addtocart),
    path('cart',views.showMyCart),
    path('removecart/<cartid>',views.removeCart),
    path('updateqty/<incr>/<cid>',views.updateQuantity),
    path('confirmorder',views.confirmorder),
    path('searchby/<val>',views.searchShoeByType),
    path('searchbyy/<vall>',views.searchShoeBySize),
    path('searchby2/<val3>',views.searchShoeByColor),
    path('searchby2/searchby2/<val3>',views.searchShoeByColor),
    path('searchby2/searchby2/searchby2/<val3>',views.searchShoeByColor),
    path('searchby2/searchby2/searchby2/searchby2/<val3>',views.searchShoeByColor),
    path('searchby2/searchby2/searchby2/searchby2/searchby2/<val3>',views.searchShoeByColor),
    path('searchby2/searchby2/searchby2/searchby2/searchby2/searchby2/<val3>',views.searchShoeByColor),
    path('placeorder',views.placeorder),
    path('placeeorder',views.placeeorder),
    path('thankyou',views.thankyou),
    path('myorders',views.myorders),
    
    
]

urlpatterns += static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)
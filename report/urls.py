from django.contrib import admin
from django.urls import path, include
from report import views
from django.contrib.auth import views as auth_views




urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('ur', views.ur, name='ur'),
    path('log', views.log, name="log"),
    path('logout', views.handlelogout, name='handlelogout'),
    path('login', views.handlelogin, name='handlelogin'),
    path('sign', views.sign, name='sign'),
    path('download', views.download, name="download"),



    # --- Razorpay & Credit Routes ---
    
    # Page where user clicks "Pay Now"
    path('buy-credits/', views.buy_credits, name='buy_credits'),
    
    # The URL Razorpay sends data to after a successful transaction
    path('payment-status/', views.payment_status, name='payment_status'),
    


]



from django.urls import path, include
from. views import *

urlpatterns=[

    path('', intro, name="intro"),
    path('home',homepage,name="home"),
    path('adduser', adduser, name="adduser"),
    path('checkuser',checkuser,name="checkuser"),
    path('admin_adduser', admin_adduser, name="admin_adduser"),
    path('admin_checkuser',admin_checkuser,name="admin_checkuser"),
    path('about',about,name="about"),
    path('contact',contact,name="contact"),
    path('termsofuse',termsofuse,name="termsofuse"),
    path('ticket',ticket, name='ticket'),
    path('payment',payment,name="payment"),
    path('Register',Register,name="Register"),
    path('admin_Register',admin_Register,name="admin_Register"),
    path('user_page',user_page,name="user_page"),
    path('admin_user_page',admin_user_page,name="admin_user_page"),
    path('user_about', user_about, name="user_about"),
    path('user_contact', user_contact, name="user_contact"),
    path('user_termsofuse', user_termsofuse, name="user_termsofuse"),
    path('home',Logout,name="Logout"),
    path('passengerlist',passengerlist,name="passengerlist"),
    path('ticketlist',ticketlist,name="ticketlist"),
]
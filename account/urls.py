from django.urls import path
from . import views
from django.contrib import admin
from django.conf.urls import include


urlpatterns = [

    path('register/',views.register, name="register"),
    path('userlogin/',views.userlogin, name="userlogin"),
    path('userlogout/',views.userlogout, name="userlogout"),

    # path('about/',views.about, name="About"),
    # path('contact/',views.contact, name="ContactUs"),
    # path('products/<int:id>',views.products, name="ViewProduct"),
    # path('track',views.track, name="TrackOrder")

    

]

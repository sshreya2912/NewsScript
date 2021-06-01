from django.urls import path
from . import views
from django.contrib import admin
from django.conf.urls import include


urlpatterns = [

    path('',views.home, name="ShopHome"),
    path('about/',views.about, name="About"),
    path('contact/',views.contact, name="ContactUs"),
    path('track',views.track, name="TrackOrder"),
    path('buisness/',views.buisness, name="Buisness"),
    path('tech/',views.technology, name="Tech"),
    path('entertainment/',views.entertainment, name="Entertainment"),
    path('sports/',views.sports, name="Sports"),
    path('health/',views.health, name="Health"),
    path('science/',views.science, name="science"),
    
   

    

]

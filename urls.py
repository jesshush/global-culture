from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('contact.html',views.contact,name="contact"),
    path('about.html',views.about,name="about"),
    path('connect.html',views.connect,name="connect"),
    path('signin.html',views.signin,name="signin"),

]

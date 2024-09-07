from django.urls import path
from . import views


urlpatterns = [
    path('hello/', views.say_hello),
    path('home/', views.home_page),
    path('about/', views.about_page),
    path('contact/', views.contact_page),

]
from django.urls import path
from .import views 

urlpatterns = [
    # path('', views.say_hello),
    path('home/', views.homepage),
    path('about/', views.about_page),
    path('contact/', views.contact_page),
    path('', views.global_home),
]
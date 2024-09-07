from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def say_hello(request):
    return HttpResponse("Hello, Django!!!!!!")

def home_page(request):
    return render(request, "index.html")

def about_page(request):
    return render(request, 'about.html')

def contact_page(request):
    return render(request, 'contact.html')

# def global_home(request):
#     return render(request, 'global_home.html')

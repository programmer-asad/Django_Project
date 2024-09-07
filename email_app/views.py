from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def show_email(request):
    return render(request, "email.html")

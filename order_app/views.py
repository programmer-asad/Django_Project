from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def order_page(request):
    return render(request, "order.html")

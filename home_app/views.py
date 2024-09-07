from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def global_home(request):
    return render(request, 'global_home.html')
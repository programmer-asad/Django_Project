from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def email_page(request):
    # return HttpResponse('This is email management app!!')
    return render(request, "email.html")

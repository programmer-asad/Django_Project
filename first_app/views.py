from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def say_hello(request):
    return HttpResponse("Hello, Django!!!!!!")

def home_page(request):
    page = {
        "title": "Homepage !! awesome",
        "content": "Welcome to the homepage"
        }
    content = {"Welcome to the homepage"}
    return render(request, "index.html", page)

def about_page(request):
    return render(request, 'about.html')

def contact_page(request):
    email = "contact@example.com"
    social_profiles = [
        "Facebook: fb.com/example",
        "Twitter: x.com/twitter",
        "Instagram: instagram.com/example",
        "Youtube: youtube.com/example"
    ]
    hq = "a"
    return render(request, 'contact.html', {"email_address": email, "socialprofiles": social_profiles, "hq": hq})

# def global_home(request):
#     return render(request, 'global_home.html')

def experiment(request, person=None):
    # if person == None:
    if person is None:
        person = "Guest"
    return render(request, "experiment.html", {"data":person})

def experiment_greet(request, person, greet):
    return render(request, "experiment.html", {"data":person, "greetings":greet})

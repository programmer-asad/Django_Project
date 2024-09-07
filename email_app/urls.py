from django.urls import path
from . import views


urlpatterns = [
    path('show/', views.email_page)
]
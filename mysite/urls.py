from django.urls import path, include
from django.shortcuts import render
from . import views


urlpatterns = [
    path('',views.home, name='home'), #three value
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
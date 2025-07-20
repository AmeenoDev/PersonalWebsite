from django.urls import path, include
from django.shortcuts import render
from . import views


urlpatterns = [
    path('',views.home, name='home'), #three value
    path('about/', views.about, name='about'),
]
def home(request):
    return render(request, 'mysite/templates/home.html')

def about(request):
    return render(request, 'mysite/templates/about.html')
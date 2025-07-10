from django.shortcuts import render

# Create your views here.

def home(request):
    x = {'name': '','age': 25, 'hobby': 'coding', 'location': 'Earth'}
    return render(request, 'home.html',x)
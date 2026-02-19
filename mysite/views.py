from django.shortcuts import render
from . models import Login
from . forms import LoginForm
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    if request.method == 'POST':
        dataform =LoginForm(request.POST)
        if dataform.is_valid():
            dataform.save()
    # username = request.POST.get('username')
    # password = request.POST.get('password')
    # data = Login(username=username,password=password)
    # data.save()
    return render(request, 'about.html',{'loginform':LoginForm()})


def contact(request):
    return render(request, 'contact.html')
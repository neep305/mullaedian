from django.shortcuts import render
from django.template import loader

# Create your views here.
def index(request):
    
    return render(request, 'auth/index.html')

def login(request):
    return render(request, 'auth/login.html')

def register(request):
    return render(request, 'auth/register.html')
from django.shortcuts import render
from home.forms import RegisterForm

# Create your views here.

def index(request):
    form = RegisterForm()


    return  render(request, 'home/index.html',{'form':form})

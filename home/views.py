from django.shortcuts import render
from home.forms import RegisterForm

#
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def index(request):
    print('in index')
    form = RegisterForm()
    login_error=""

    if request.method == 'POST':
        print("posted")
        if 'A' in request.POST:
            print('in login form')
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(username=username,password=password)

            if user:
                print("user authenticated")
                if user.is_active :
                    login(request,user)
                    return HttpResponse("User Logged in")

                else:
                    return HttpResponse("Account not Active")
            else:
                login_error = "Invalid Username or Password"
                return  render(request, 'home/index.html',{'form':form,'login_error':login_error})


        elif 'B' in request.POST:
            form = RegisterForm(request.POST)

            if form.is_valid():
                user = form.save()
                user.set_password(user.password)
                user.save()
                form = RegisterForm()
                return render(request, 'home/index.html',{'form':form})
            else:
                print(form.errors)
                return render(request, 'home/index.html',{'form':form})


    return  render(request, 'home/index.html',{'form':form,'login_error':login_error})




@login_required
def dashboard(request):
    return render(request, 'home/dashboard.html')

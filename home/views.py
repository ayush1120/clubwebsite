from django.shortcuts import render
from home.forms import RegisterForm

# Create your views here.

def index(request):
    form = RegisterForm()

    if request.method == 'POST':
        if 'A' in request.POST:
            nothing()

        elif 'B' in request.POST:
            form = RegisterForm(request.POST)

            if form.is_valid():
                user = form.save()
                user.set_password(user.password)
                user.save()
                form = RegisterForm()
                return render(request, 'home/index.html',{'form':form})

    return  render(request, 'home/index.html',{'form':form})

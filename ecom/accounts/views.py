from django.shortcuts import render
from accounts.models import Newusers
from accounts.forms import Newuserform,Baseuser
from django.core import validators
# for user authentication
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.

# index view

def index(request):
    return render(request,'accounts/index.html')
    

# registration view and request handling

def register(request):

    registered = False
    
    if request.method == 'POST':
        user_form = Baseuser(data=request.POST)
        user_pic = Newuserform(data=request.POST)
        if user_form.is_valid() and user_pic.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            userpic = user_pic.save(commit=False)
            userpic.user = user

            if 'user_pic' in request.FILES:
                userpic.user_pic = request.FILES['user_pic']
            userpic.save()
            registered = True
            return render(request,'accounts/index.html',{'registered':registered})

        else:
            context_dict1 = {'error1':user_form.errors,'error2':user_pic.errors}
            return render(request,'accounts/signup.html',context_dict1)

    else:
        user_form = Baseuser()
        user_pic = Newuserform()

        context_dict = {'user_form':user_form,'user_pic':user_pic,'registered':registered,'error1':user_form.errors,'error2':user_pic.errors}
        return render(request,'accounts/signup.html',context_dict)

# login view function

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return render(request,'accounts/special.html')
            else:
                HttpResponse("Account not active")
        else:
            print("Someone tried to login and failed")
            print("Username:{} and password {}".format(username,password))
            return HttpResponse("Invalid login details.")
    else:
        return render(request,'accounts/login.html') 


def user_logout(request):
    logout(request)
    return render(request,'accounts/index.html')

# special view

@login_required
def special(request):
    return render(request,'accounts/special.html')
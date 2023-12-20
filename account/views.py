from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .models import *
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def sign_in(request):
    if "password" in request.GET:
        data = request.GET
        User = get_user_model()
        user = User.objects.get(email=data['email'])
        password = data['password']
        auth_user = authenticate(request, username=user, password=password)
        if user is not None:
            login(request, auth_user)
            return redirect("home")
        else:
            print("Login failed")
    # print(user.base_role)
    return render(request, 'ui-elements/auth-signin.html')

def sign_up(request):
    if request.method == 'POST':
        data = request.POST
        User = get_user_model()
        if data['password'] == data['confirm_password']:
            match data['radio']:
                case 'admin':
                    admin = Admin.objects.create_user(username=data['name'], email=data['email'], password=data['password'], role=data['radio'], is_superuser=True)
                case 'colleague':
                    colleague = Colleague.objects.create_user(username=data['name'], email=data['email'], password=data['password'], role=data['radio'])
                case 'customer':
                    customer = Customer.objects.create_user(username=data['name'], email=data['email'], password=data['password'], role=data['radio'])
                case 'freelancer':
                    freelancer = Freelancer.objects.create_user(username=data['name'], email=data['email'], password=data['password'], role=data['radio'])
            return redirect('sign_in')

        else:
            print(400)
        
    return render(request, 'ui-elements/auth-signup.html')

def log_out(request):
    logout(request)
    return redirect('sign_in')

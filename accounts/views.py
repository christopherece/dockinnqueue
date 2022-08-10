import email
from multiprocessing import context
from django.shortcuts import render, redirect
from queues.models import Queue
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is already taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email is already registered')
                    return redirect('login')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    #Login After
                    auth.login(request, user)
                    messages.success(request, 'You are now registered')
                    return redirect('dashboard')

        else:
            messages.error(request, 'Password did not match, Try again')
            return redirect('register')

    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')

    else:
        return render(request, 'accounts/login.html')

@login_required(login_url='login')
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now log out')
        return redirect('login')

@login_required(login_url='login')
def dashboard(request):
    queueLists = Queue.objects.filter(technician__contains = request.user.username).values() | Queue.objects.filter(technician__startswith = 'Not Assigned').values()
    print(request.user.username)
    context = {
        'queueLists': queueLists,
    }
    return render(request, 'accounts/dashboard.html', context)

    

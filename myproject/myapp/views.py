# imports messages error checking module
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
# imports data from database registered users 
from django.contrib.auth.models import User, auth
from .models import Feature
# Create your views here.

def index(request):
    # Displaying all items inside db
    features = Feature.objects.all()
    return render(request, "index.html", {"features": features})

def form(request):
    return render(request, "form.html")
        
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            # Checks if the email exists on the users being the users in the db 
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Usersame already exists')    
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password) 
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password not the same')    
            return redirect('register')    
    else:
        return render(request, 'register.html')    

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        
        user = auth.authenticate(username=username, password=password)
        # checks f users is registered on our platform and

        if user is not None:
             auth.login(request, user)
             return redirect('/')
        else:
            messages.info(request, 'Credentails invalid')
            return redirect('login')

    else:
        return render(request, "login.html") 

def logout(request):
    auth.logout(request)
    return redirect('/')                      

def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    print(amount_of_words)
    return render(request, 'counter.html', {'count': amount_of_words})
from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
def signup(request):
    if request.method == 'POST':
        user = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        zip = request.POST['zip']

        x = User(username = user , email = email ,password = password , zip = zip)
        x.save()
        return redirect('/')
    return render(request,'form.html')

def login(request):
    if request.method =='POST':
        user = request.POST['username']
        password = request.POST['password']
        x = auth.authenticate(username = user, password = password)
        if x is None:
            return redirect('login')
        else:
            print('login successfull...')
            return redirect('/')
    else:
        return render(request, 'login.html')

    return render(request, 'login.html')
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def userlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request,user)
            messages.info(request, 'You have sucessfuly logged in')
            #redirect means sending the controls to that view
            return redirect('/shop/')
        else:
            messages.info(request, 'account does not exit ')
            return render(request,'account/login.html')
    else:
        return render(request,'account/login.html')
def userlogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/shop/')
def register(request):
    if request.method=="POST":
        username=request.POST['username']
        user_email=request.POST['user_email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        password=request.POST['password']
        cp=request.POST['cpassword']
        c=0
        if len(password)<6:
            messages.info(request, 'Passwords too short!')
            c=1
        if len(username)<5:
            messages.info(request, 'Please select a username with more than 5 characters!')
            c=1
        if password!=cp:
            messages.info(request, 'Passwords do not match!')
            c=1
        if c==1:
            return render(request,'account/register.html')
        
        else:
         user = User.objects.create_user(username, user_email, password)
         user.first_name = fname
         user.last_name = lname
         user.save()
         messages.info(request, 'Your account has been succesfuly created please login into your account!')
         return render(request,'account/login.html')
        
        
    else:
        return render(request,'account/register.html')

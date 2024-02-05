from django.shortcuts import render,redirect
from students.models import Student,CustomUser
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        c=request.POST['c']
        e=request.POST['e']
        f=request.POST['f']
        l=request.POST['l']
        a=request.POST['a']
        n=request.POST['n']
        if (p==c):
            r=CustomUser.objects.create_user(username=u,password=p,email=e,first_name=f,last_name=l,place=a,phone=n)
            r.save()
            return redirect ('books:home')

        else:
            return HttpResponse("Passwords are not same")

    return render(request,'register.html')
def user_login(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        l=authenticate(username=u,password=p)
        if l:
            login(request,l)
            return redirect('books:home')
        else:
            return HttpResponse("Invalid credentials")
    return render(request,'login.html')
@login_required
def viewstudents(request):
    k=Student.objects.all()
    return render(request,'viewstudents.html',{'s':k})
@login_required
def user_logout(request):
    logout(request)
    return redirect('students:login')

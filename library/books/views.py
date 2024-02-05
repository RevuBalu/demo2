from django.shortcuts import render
from books.models import Book
from django.http import HttpResponse
from books.forms import bookform
from django.db.models import Q
from django.contrib.auth.decorators import login_required
import math
# Create your views here.
def home(request):
    return render(request,'home.html')
@login_required
def addbooks(request):
    if(request.method=="POST"):   #after submission
        t=request.POST['t']
        a=request.POST['a']
        p=request.POST['p']
        f=request.FILES['f']
        i=request.FILES['i']
        b=Book.objects.create(title=t,author=a,price=p,pdf=f,cover=i)
        b.save()
        return viewbooks(request)
    return render(request,'addbooks.html')
@login_required
def viewbooks(request):
    k=Book.objects.all()
    return render(request,'viewbooks.html',{'b':k})
@login_required
def addbooks1(request):
    if (request.method=="POST"): #after form submission
        form=bookform(request.POST)  #creates form object initialized with values inside request.POST
        if form.is_valid():
            form.save()  #saves form object in db model Book
            return viewbooks(request)
    form=bookform() #creates empty form objects
    return render(request,'addbooks1.html',{'form':form})
@login_required
def fact(request):
     # if (request.method=="POST"):  # after submission
     #    num=int(request.POST['n'])
     #
     #    f = math.factorial(num)
     #    return render(request,'fact.html',{'fact':f})
     #
     # return render(request,'fact.html')
     if (request.method=="POST"):
         num=int(request.POST['n'])
         f=1
         for i in range(1,num+1):
             f=f*i
         return render(request, 'fact.html', {'fact': f})
     return render(request,'fact.html')
@login_required
def detail(request,p):
    d=Book.objects.get(id=p)
    return render(request,'detail.html',{'b':d})
@login_required
def delete(request,p):
    d=Book.objects.get(id=p)
    d.delete()
    return viewbooks(request)
@login_required
def edit(request,p):
    e=Book.objects.get(id=p)
    if (request.method=="POST"):    #after submission
        form=bookform(request.POST,request.FILES,instance=e)
        if form.is_valid():
            form.save()    #save form object in db model Book
            return viewbooks(request)
    form=bookform(instance=e)
    return render(request,'edit.html',{'form':form})
@login_required
def search(request):
    s=None
    q=""
    if (request.method=="POST"):
        q=request.POST['q']
        s=Book.objects.filter(Q(title__icontains=q)|Q(author__icontains=q))
    return render(request,'search.html',{'c':q,'b':s})



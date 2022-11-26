from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
# Create your views here.
def feed(request):
    posts=Post.objects.all()
    context={'posts':posts}
    return render (request,'feed.html',context)  #para que se encuentre la carpeta de los statics , el nombre de la carpeta
    #debe ser templates

def profile(request):

    return render(request,'profile.html')

def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            messages.success(request,f'usuario {username} creado')
            return redirect('feed')
    else:
        form=UserRegisterForm()
    context={'form':form}
    return render(request,'register.html',context)

'''
def login(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            messages.success(request,f'usuario {username} creado')
            return redirect('feed')
    else:
        form=UserRegisterForm()
    context={'form':form}
    return render(request,'login.html',context)
'''

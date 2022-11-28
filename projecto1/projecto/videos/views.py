from django.shortcuts import render, redirect,get_object_or_404
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.models import User
# Create your views here.
def feed(request):
    '''
    if request.user.is_authenticated():
        current_user=get_object_or_404(User,pk=request.user.pk)
    '''
    user=request.user  #current user
    #movies=Movie.objects.all()[0:3] no incluye el ultimo elemento (el 3)
    movies1_3=Movie.objects.all()[0:3]
    movies4_6=Movie.objects.all()[3:6]
    movies7_9=Movie.objects.all()[6:9]
    #print(movies)
    #displayed_movies=(movies[0:2],movies[3:5],movies[6:8])
    #print('---------------')
    #print(displayed_movies)
    context={'user':user,'movies1_3':movies1_3,'movies4_6':movies4_6,'movies7_9':movies7_9}
    return render (request,'feed.html',context)  #para que se encuentre la carpeta de los statics , el nombre de la carpeta
    #debe ser templates

def profile(request):
    #current_user=request.user
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

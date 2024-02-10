from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm



def home(request):
    return render (request,'home.html',{})


def signup(request):
    if request.method == 'POST':
       form = CustomUserCreationForm(request.POST)
       if form.is_valid():
           form.save
           username = form.cleaned_data.get('username')
           password = form.cleaned_data.get('password')
           user = authenticate(username = username, password = password)
           login(request,user)
           return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render (request,'signup.html',{'form':form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
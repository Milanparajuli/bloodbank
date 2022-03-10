from django.shortcuts import render
from .forms import UserCreationForm

# Create your views here.

def signin(request):
    return render(request,'login.html')

def signup(request):
    form = UserCreationForm()
    contex ={
        'form':form
    }
    return render(request,'signup.html',contex)

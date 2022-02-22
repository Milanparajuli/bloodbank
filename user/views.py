from django.shortcuts import render

# Create your views here.

def signin(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')

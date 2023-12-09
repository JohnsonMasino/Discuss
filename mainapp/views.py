from django.shortcuts import render

def Home(request):
    context = {}
    return render(request, 'letstalk/main.html', context)

def Login(request):
    context = {}
    return render(request, 'letstalk/login.html', context)

def SignUp(request):
    return render(request, 'letstalk/signup.html')
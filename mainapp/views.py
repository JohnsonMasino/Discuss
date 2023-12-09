from django.shortcuts import render

def Home(request):
    context = {}
    return render(request, 'mainapp/main.html', context)

def Login(request):
    context = {}
    return render(request, 'mainapp/login.html', context)

def SignUp(request):
    return render(request, 'mainapp/signup.html')
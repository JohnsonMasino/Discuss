from django.shortcuts import render
from rest_framework.views import APIView
from . serializers import UserSerializer
from rest_framework.response import Response

def Home(request):
    context = {}
    return render(request, 'mainapp/main.html', context)

def Login(request):
    context = {}
    return render(request, 'mainapp/login.html', context)

def SignUp(request):
    return render(request, 'mainapp/signup.html')

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
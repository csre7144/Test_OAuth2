# from django.shortcuts import render
# from .serializers import UserFormSerializer
# from .models import UserForm

# Create your views here.
# def home(request):
#     data = UserFormSerializer()
#     if request.method == 'POST':
#         data = UserFormSerializer(data=request.POST)
#         if data.is_valid():
#             data.save()
        
#     context = { data:'data'}
#     return render(request, 'index.html', context)


from django.shortcuts import render, redirect
from rest_framework.parsers import JSONParser
from .serializers import UserSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def home(request):
    return render(request, 'index.html')

def register_list(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return redirect('home')  # Redirect to avoid resubmission on refresh
        return Response(serializer.errors, status=400)
    else:
        serializer = UserSerializer()
    
    return render(request, 'register.html', {'serializer': serializer})

def signin_list(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('signin_list')
    return render(request, 'signin.html')

from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'frontview.html')
def login(request):
    return render(request,'login.html')
def sign(request):
    return render(request,'signup.html')
def homes(request):
    return render(request,'home.html')

from django.shortcuts import render

def home(request):
    return render(request, 'Art/home.html')

def Profile(request):
    return render(request, 'Art/profile.html')
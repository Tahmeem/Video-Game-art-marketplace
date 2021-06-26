from django.shortcuts import render
from .models import artWork

def home(request):
    context = {
        'Drawings': artWork.objects.all()
    }
    return render(request, 'Art/home.html', context)

def Profile(request):
    return render(request, 'Art/profile.html')
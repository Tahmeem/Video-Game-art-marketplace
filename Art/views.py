from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import artWork

def home(request):
    context = {
        'Drawings': artWork.objects.all()
    }
    return render(request, 'Art/home.html', context)

class ArtListView(ListView):
    model = artWork
    template_name = 'Art/home.html'
    context_object_name = 'Drawings'
    ordering = ['-date_posted']

class ArtDetailView(DetailView):
    model = artWork

def Profile(request):
    return render(request, 'Art/profile.html')
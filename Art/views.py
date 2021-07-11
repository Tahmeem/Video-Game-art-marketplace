from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import artWork
from django.db.models import F


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

class ArtCreateView(CreateView):
    model = artWork
    template_name = 'Art/art_form.html'
    fields = [
        'title',
        'description',
        'Price',
        'image',
        'creator_email',
    ]
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
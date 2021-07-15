from django.views.generic import \
    ListView, \
    DetailView,\
    CreateView, \
    UpdateView
from .models import artWork,suggestArt
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin



class ArtListView(ListView):
    model = artWork
    template_name = 'Art/home.html'
    context_object_name = 'Drawings'
    ordering = ['-date_posted']

class HelpListView(ListView):
    model = artWork
    template_name = 'Art/Help.html'


class ArtDetailView(DetailView):
    model = artWork

class ArtCreateView(LoginRequiredMixin,CreateView):
    model = artWork
    template_name = 'Art/art_form.html'
    fields = [
        'title',
        'description',
        'Price',
        'image',
        'creator_email',
    ]
    login_url = '/login/'

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

    def test_func(self):
        art = self.get_object()
        if self.request.user == art.author:
            return True
        return False
class ArtUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = artWork
    template_name = 'Art/art_form.html'
    fields = [
        'title',
        'description',
        'Price',
        'image',
        'creator_email',
    ]
    login_url = '/login/'
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

class ArtSuggestionCreate(LoginRequiredMixin,CreateView):
    model = suggestArt
    template_name = 'Art/art_suggest.html'
    fields = [
        'title',
        'suggestion',
        'creator'
    ]
    login_url = '/login/'
from django.views.generic import \
    ListView, \
    DetailView,\
    CreateView, \
    UpdateView, \
    DeleteView
from .models import artWork,suggestArt,reportArt
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.shortcuts import redirect
from django.http import Http404

def search(request):
    if request.method == "GET":
        search_name = request.GET.get('Search')
        try:
            search_result = artWork.objects.filter(title=search_name)
            print(search_result[0])
            return redirect("artwork-visual",  search_result[0].id)
        except Exception as e:
            raise Http404

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

class ArtVisualView(DetailView):
    model = artWork
    template_name = 'Art/art_visual.html'

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
    def test_func(self):
        art = self.get_object()
        if self.request.user == art.creator:
            return True
        return False

class ArtSuggestionCreate(LoginRequiredMixin,CreateView):
    model = suggestArt
    template_name = 'Art/art_suggest.html'
    fields = [
        'title',
        'suggestion',
        'creator'
    ]
    login_url = '/login/'

class ArtReportView(LoginRequiredMixin,CreateView):
    model = reportArt
    template_name = 'Art/art_report.html'
    fields = [
        'title',
        'details',
        'creator'
    ]
    login_url = '/login/'

class ArtDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = artWork
    login_url = '/login/'
    success_url = '/'
    def test_func(self):
        art = self.get_object()
        if self.request.user == art.creator:
            return True
        return False
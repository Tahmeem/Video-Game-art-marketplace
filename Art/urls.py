from django.urls import path
from .views import ArtListView, ArtDetailView, ArtCreateView,HelpListView,ArtSuggestionCreate,ArtUpdateView
from . import views
urlpatterns = [
    path('', ArtListView.as_view(), name='artwork-home'),
    path('art/<int:pk>/', ArtDetailView.as_view(), name='artwork-detail'),
    path('art/new/', ArtCreateView.as_view(), name='artwork-create'),
    path('art/<int:pk>/update', ArtUpdateView.as_view(), name='artwork-update'),
    path('art/help/', HelpListView.as_view(), name='artwork-help'),
    path('art/suggest/', ArtSuggestionCreate.as_view(), name='artwork-suggest'),
]

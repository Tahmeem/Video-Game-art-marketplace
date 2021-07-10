from django.urls import path
from .views import ArtListView, ArtDetailView, ArtCreateView
from . import views
urlpatterns = [
    path('', ArtListView.as_view(), name='artwork-home'),
    path('art/<int:pk>/', ArtDetailView.as_view(), name='artwork-detail'),
    path('art/new/', ArtCreateView.as_view(), name='artwork-create'),
]

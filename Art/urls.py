from django.urls import path
from .views import ArtListView, ArtDetailView
from . import views
urlpatterns = [
    path('', ArtListView.as_view(), name='artwork-home'),
    path('art/<int:pk>/', ArtDetailView.as_view(), name='artwork-detail'),
    path('profile/', views.Profile, name='artwork-profile'),
]

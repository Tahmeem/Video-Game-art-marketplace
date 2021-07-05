from django.urls import path
from .views import ArtListView
from . import views
urlpatterns = [
    path('', ArtListView.as_view(), name='artwork-home'),
    path('profile/', views.Profile, name='artwork-profile'),
]

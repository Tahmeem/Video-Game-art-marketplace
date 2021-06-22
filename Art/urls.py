from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='artwork-home'),
    path('profile/', views.Profile, name='artwork-profile'),
]

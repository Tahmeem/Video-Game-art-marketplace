from django.urls import path
from .views import \
    ArtListView, \
    ArtDetailView, \
    ArtCreateView,\
    HelpListView,\
    ArtSuggestionCreate,\
    ArtUpdateView,\
    ArtDeleteView,\
    ArtReportView,\
    ArtVisualView

urlpatterns = [
    path('', ArtListView.as_view(), name='artwork-home'),
    path('art/<int:pk>/', ArtDetailView.as_view(), name='artwork-detail'),
    path('art/<int:pk>/visual/', ArtVisualView.as_view(), name='artwork-visual'),
    path('art/new/', ArtCreateView.as_view(), name='artwork-create'),
    path('art/<int:pk>/update/', ArtUpdateView.as_view(), name='artwork-update'),
    path('art/<int:pk>/delete/', ArtDeleteView.as_view(), name='artwork-delete'),
    path('art/help/', HelpListView.as_view(), name='artwork-help'),
    path('art/report/', ArtReportView.as_view(), name='artwork-report'),
    path('art/suggest/', ArtSuggestionCreate.as_view(), name='artwork-suggest'),
]

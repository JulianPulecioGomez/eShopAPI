from django.urls import path
from apps.tags.api.views import TagListView, TagDetailView, TagCreateView

urlpatterns = [
    path('list/', TagListView.as_view(), name='TagList'),
    path('detail/<pk>', TagDetailView.as_view(), name='TagDetail'),
    path('create', TagCreateView.as_view(), name='TagCreate'),
]
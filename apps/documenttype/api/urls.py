from django.urls import path
from apps.documenttype.api.views import documenttype_list_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('list', documenttype_list_view.as_view(), name='documentType.list'),
]
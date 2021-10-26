from django.urls import path
from apps.users.api.views import UserListView ,UserDetailView, UserRegistrationView, UserLogOut
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register', UserRegistrationView.as_view(), name='register'),
    path('log_out', UserLogOut.as_view(), name='log_out'),
    path('list', UserListView.as_view(), name='user.list'),
    path('detail/<pk>', UserDetailView.as_view(), name='user.detail'),
]
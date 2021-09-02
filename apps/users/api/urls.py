from django.urls import path
from apps.users.api.views import registration_view

app_name = 'account'

urlpatterns = [
    path('register', registration_view, name='register'),
]
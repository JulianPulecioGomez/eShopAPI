from django.urls import path
from apps.users.api.views import user_list_view ,user_detail_view, registration_view, log_out

app_name = 'account'

urlpatterns = [
    path('list', user_list_view.as_view(), name='user.list'),
    path('detail/<pk>', user_detail_view.as_view(), name='user.detail'),
    path('register', registration_view.as_view(), name='register'),
    path('log_out', log_out.as_view(), name='log_out'),
]
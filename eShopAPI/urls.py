from django.contrib import admin
from django.urls import path,include,re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('apps.users.api.urls')),
    path('document_type/', include('apps.documenttype.api.urls'))
]

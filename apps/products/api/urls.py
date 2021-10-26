from django.urls import path
from apps.products.api.views import ProductListView, ProductDetailView, ProductCreateView

urlpatterns = [
    path('list/', ProductListView.as_view(), name='ProductList'),
    path('detail/<pk>', ProductDetailView.as_view(), name='ProductDetail'),
    path('create', ProductCreateView.as_view(), name='ProductCreate'),
]
from django.contrib import admin
from django.urls import path, include, re_path
from apps.documentType.api.views import DocumentTypeViewSet
from apps.tags.api.views import TagViewSet
from apps.products.api.views import ProductViewSet
from apps.users.api.views import UserViewSet, UserRegistrationViewSet
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework.response import Response
from rest_framework import status
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'user', UserViewSet, basename='user')
router.register(r'userRegistration', UserRegistrationViewSet, basename='userRegistration')
router.register(r'documentType', DocumentTypeViewSet, basename='documentType')
router.register(r'tag', TagViewSet, basename='tag')
router.register(r'product', ProductViewSet, basename='product')


class TokenBlackList(APIView):
    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'refresh_token': openapi.Schema(
                type=openapi.TYPE_STRING,
            )
        }
    ))
    def post(self, request):
        try:
            refresh_token = request.POST.get("refresh_token")
            refresh_token = RefreshToken(refresh_token)
            refresh_token.blacklist()
            return Response({'message': 'Token Deleted Succesfully'}, status=status.HTTP_200_OK)
        except:
            return Response({'message': 'There was and error'}, status=status.HTTP_400_BAD_REQUEST)


urlpatterns = [
    re_path('^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin', admin.site.urls),
    path('authentication', TokenObtainPairView.as_view(), name='authentication_obtain_pair'),
    path('authentication/refresh', TokenRefreshView.as_view(), name='authentication_refresh'),
    path('authentication/logout', TokenBlackList.as_view(), name='authentication_token_black_list'),
]

urlpatterns += router.urls

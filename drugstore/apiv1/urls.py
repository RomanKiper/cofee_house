from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import SimpleRouter

from .views import ProductViewSet, CategoryViewSet, AuthToken

api_router = SimpleRouter()
api_router.register(r'products', ProductViewSet)
api_router.register(r'categories', CategoryViewSet)


urlpatterns = [
    path('', include(api_router.urls)),
    path('login/', AuthToken.as_view())
]
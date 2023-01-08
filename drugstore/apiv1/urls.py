from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import ProductViewSet, CategoryViewSet

api_router = SimpleRouter()
api_router.register(r'products', ProductViewSet)
api_router.register(r'categories', CategoryViewSet)


urlpatterns = [
    path('', include(api_router.urls))
]
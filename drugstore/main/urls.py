from django.urls import path

from .views import IndexTemplateView, ProductListView, WorkScheduleListView, AboutTemplateView


urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('about/', AboutTemplateView.as_view(), name='about'),
    path('products/', ProductListView.as_view(), name='products'),
    path('store/', WorkScheduleListView.as_view(), name='store'),
]
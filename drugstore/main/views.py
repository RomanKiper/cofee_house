from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime

from django.views.generic import TemplateView, ListView

from .models import Product, WorkSchedule


class IndexTemplateView(TemplateView):
    template_name = 'main/index.html'


class AboutTemplateView(TemplateView):
    template_name = 'main/about.html'


class ProductListView(LoginRequiredMixin, ListView):
    template_name = 'main/products.html'
    context_object_name = 'products'
    model = Product
    login_url = '/signin/'

    def get_queryset(self):
        from itertools import zip_longest
        objs = Product.objects.filter(is_published=True)
        objs = iter(objs)
        return list(zip_longest(objs, objs))


class WorkScheduleListView(ListView):
    template_name = 'main/store.html'
    context_object_name = 'week'
    model = WorkSchedule

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['weekday'] = datetime.today().isoweekday() + 6
        return context
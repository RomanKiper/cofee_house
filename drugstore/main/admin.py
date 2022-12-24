from django.contrib import admin

from .models import Category, Product, WorkSchedule


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published')
    search_fields = ('name', )
    list_filter = ('is_published', )
    ordering = ('is_published', 'name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_published')
    list_filter = ('category', 'is_published')
    search_fields = ('name', )
    ordering = ('is_published', 'name')


@admin.register(WorkSchedule)
class WorkScheduleAdmin(admin.ModelAdmin):
    list_display = ('week_day', 'opening_time', 'closing_time')
    search_fields = ('week_day', )
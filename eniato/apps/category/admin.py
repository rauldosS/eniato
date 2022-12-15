from django.contrib import admin

from apps.category.models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'category_type', 'name')

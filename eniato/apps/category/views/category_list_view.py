from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.category.repositories import CategoryRepository


class CategoryListView(LoginRequiredMixin, ListView):

    template_name = 'category/category-list.html'
    context_object_name = 'categories'
    repository = CategoryRepository()

    def get_queryset(self):
        return self.repository.get_by_user(self.request.user)

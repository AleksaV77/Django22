from itertools import product

from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseForbidden
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Product, Category
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from config.settings import CACHE_ENABLED
from .services import CategoryServices, get_products_from_cache


@method_decorator(cache_page(60), name='dispatch')
class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        if CACHE_ENABLED:
            return get_products_from_cache()
        else:
            return Product.objects.filter(unpublish_product=True)


@method_decorator(cache_page(60), name='dispatch')
class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")
    permission_required = "catalog.add_product"

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")
    permission_required = "catalog.change_product"

    def get_success_url(self):
        return reverse("catalog:product_detail", args=[self.kwargs.get("pk")])

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm("catalog.can_unpublish_product"):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:home")
    permission_required = "catalog.delete_product"


class ContactsView(TemplateView):
    template_name = "catalog/contacts.html"


@method_decorator(cache_page(60), name='dispatch')
class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'category_list'

@method_decorator(cache_page(60), name='dispatch')
class CategoryDetailView(DetailView):
    model = Category
    template_name = "catalog/category_detail.html"
    context_object_name = "category_detail"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs.get('pk')
        context['category_id'] = category_id
        context['category_name'] = CategoryServices.get_category_name(category_id)
        context['all_products'] = CategoryServices.get_all_products_in_category(category_id)
        return context


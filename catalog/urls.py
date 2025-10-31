from django.urls import path
from django.views.decorators.cache import cache_page

from . import views
from .views import (
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    ContactsView, CategoryDetailView, CategoryListView
)

app_name = "catalog"

urlpatterns = [
    path("product/", cache_page(60)(ProductListView.as_view()), name="home"),
    path(
        "product_detail/<int:pk>/", cache_page(60)(ProductDetailView.as_view()), name="product_detail"
    ),
    path("product/create/", ProductCreateView.as_view(), name="product_create"),
    path(
        "product/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"
    ),
    path(
        "product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"
    ),
    path('product/category_detail/<int:pk>', CategoryDetailView.as_view(), name='category_detail'),
    path('product/category_list/', CategoryListView.as_view(), name='category_list'),
    path("contacts/", ContactsView.as_view(), name="contacts"),
]

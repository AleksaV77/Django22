from django.urls import path
from . import views
from .views import ProductListView, ProductDetailView, ContactsView

app_name = 'catalog'

urlpatterns = [
    path("", ProductListView.as_view(), name="home"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("product_detail/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
]

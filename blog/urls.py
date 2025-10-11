from django.urls import path
from . import views
from .views import BlogsListView, BlogsCreateView, BlogsDetailView, BlogsUpdateView, BlogsDeleteView

app_name = 'blog'

urlpatterns = [
    path("blogs_list/", BlogsListView.as_view(), name="blogs_list"),
    path("blogs_detail/<int:pk>/", BlogsDetailView.as_view(), name="blogs_detail"),
    path("blogs/create", BlogsCreateView.as_view(), name="blogs_create"),
    path("blogs/<int:pk>/update/", BlogsUpdateView.as_view(), name="blogs_update"),
    path("blogs/<int:pk>/delete/", BlogsDeleteView.as_view(), name="blogs_delete"),
]
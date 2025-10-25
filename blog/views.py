from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin

from blog.forms import BlogsForm
from blog.models import Blogs


class BlogsListView(ListView):
    model = Blogs
    template_name = "blog/blogs_list.html"
    context_object_name = "blog"

    def get_queryset(self):
        return Blogs.objects.filter(published=True)


class BlogsDetailView(DetailView):
    model = Blogs

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_counter += 1
        self.object.save()
        return self.object


class BlogsCreateView(LoginRequiredMixin, CreateView):
    model = Blogs
    form_class = BlogsForm
    success_url = reverse_lazy("blog:blogs_list")


class BlogsUpdateView(LoginRequiredMixin, UpdateView):
    model = Blogs
    form_class = BlogsForm
    success_url = reverse_lazy("blog:blogs_list")

    def get_success_url(self):
        return reverse("blog:blogs_detail", args=[self.kwargs.get("pk")])


class BlogsDeleteView(LoginRequiredMixin, DeleteView):
    model = Blogs
    success_url = reverse_lazy("blog:blogs_list")

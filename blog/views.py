from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from blog.models import Blogs

class BlogsListView(ListView):
    model = Blogs
    template_name = 'blog/blogs_list.html'
    context_object_name = 'blog'

    def get_queryset(self):
        return Blogs.objects.filter(published=True)


class BlogsDetailView(DetailView):
    model = Blogs

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_counter += 1
        self.object.save()
        return self.object

class BlogsCreateView(CreateView):
    model = Blogs
    fields = ("title", "blogs_description", "image")
    success_url = reverse_lazy('blog:blogs_list')


class BlogsUpdateView(UpdateView):
    model = Blogs
    fields = ("title", "blogs_description", "image")
    success_url = reverse_lazy('blog:blogs_list')

    def get_success_url(self):
        return reverse('blog:blogs_detail', args=[self.kwargs.get('pk')])

class BlogsDeleteView(DeleteView):
    model = Blogs
    success_url = reverse_lazy('blog:blogs_list')

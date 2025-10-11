from django.contrib import admin
from .models import Blogs

@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ("title", "blogs_description", "view_counter")
    search_fields = ("title", "created_at")

from django.contrib import admin
from .models import Product, Category
@admin.register(Category)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name',)
    search_fields = ('category_name', 'category_description',)

@admin.register(Product)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('product_name', 'product_description',)

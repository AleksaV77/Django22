from .models import Category, Product
from config.settings import CACHE_ENABLED
from django.core.cache import cache


def get_products_from_cache():
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = "product_list"
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products


class CategoryServices:

    @staticmethod
    def get_category_name(category_id):
        # Получаем название продукта по его ID
        category = Category.objects.get(id=category_id)
        return f"{category.category_name}"

    @staticmethod
    def get_all_products_in_category(category):
        # Получаем список всех продуктов в указанной категории
        products = Product.objects.filter(category=category)
        return products

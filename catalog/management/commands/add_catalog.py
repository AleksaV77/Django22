from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Add test books to the database"

    def handle(self, *args, **kwargs):
        category, _ = Category.objects.get_or_create(
            category_name="Ноутбуки", category_description="Ноутбуки"
        )

        products = [
            {
                "product_name": "HUAWEI MateBook D16",
                "product_description": 'D16 2024/16"/Core i5-13420H/16/512/Win/Space Gray',
                "category": category,
                "price": "62000",
            },
            {
                "product_name": "Apple MacBook",
                "product_description": "Air 13 M1 8/256 Space Gray",
                "category": category,
                "price": "60000",
            },
        ]

        for product_data in products:
            products, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully added product: {products.product_name}"
                    )
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f"Product already exists: {products.product_name}"
                    )
                )

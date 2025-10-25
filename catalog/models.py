from django.db import models

from users.models import User


class Category(models.Model):
    category_name = models.CharField(max_length=50, verbose_name="Категория продукта")
    category_description = models.CharField(max_length=250, verbose_name="Описание")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f"{self.category_name} {self.category_description}"


class Product(models.Model):
    product_name = models.CharField(max_length=50, verbose_name="Наименование продукта")
    product_description = models.CharField(max_length=250, verbose_name="Описание")
    img = models.ImageField(
        upload_to="images",
        blank=True,
        null=True,
        verbose_name="Фото",
        help_text="Загрузите фотографию",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        related_name="products",
        null=True,
        blank=True,
    )
    price = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    unpublish_product = models.BooleanField(default=False, verbose_name="Публикация")
    owner = models.ForeignKey(
        User, verbose_name="Владелец", blank=True, null=True, on_delete=models.SET_NULL
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
        ]

    def __str__(self):
        return f"{self.product_name} {self.product_description}"

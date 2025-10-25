from django.db import models


class Blogs(models.Model):
    title = models.CharField(max_length=50, verbose_name="заголовок")
    blogs_description = models.CharField(max_length=250, verbose_name="содержимое")
    image = models.ImageField(
        upload_to="image",
        blank=True,
        null=True,
        verbose_name="Фото",
        help_text="Загрузите фотографию",
    )
    created_at = models.DateField(auto_now_add=True)
    published = models.BooleanField(default=True, verbose_name="Опубликовано")
    view_counter = models.PositiveIntegerField(
        verbose_name="Счетчик просмотров",
        help_text="Укажите количество просмотров",
        default=0,
    )

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __str__(self):
        return f"{self.title} {self.blogs_description}"

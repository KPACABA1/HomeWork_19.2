from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(
        max_length=50, verbose_name="Наименование", help_text="Наименование продукта"
    )
    Description = models.TextField(
        verbose_name="Описание", help_text="Описание продукта"
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Наименование",
        help_text="Наименование продукта",
    )
    Description = models.TextField(
        verbose_name="Описание",
        help_text="Описание продукта",
    )
    Image = models.ImageField(
        upload_to="/products",
        verbose_name="Изображение (превью)",
        null=True,
        blank=True,
        help_text="Изображение продукта",
    )
    Category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        null=True,
        blank=True,
        related_name="products",
    )
    purchase_price = models.IntegerField(
        verbose_name="Цена за покупку",
        help_text="Цена за покупку продукта",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания (записи в БД)",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата последнего изменения (записи в БД)",
    )

    def __str__(self):
        return f"{self.name} - {self.purchase_price}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

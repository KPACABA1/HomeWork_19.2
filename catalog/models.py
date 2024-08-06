from django.db import models

from users.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(
        max_length=50, verbose_name="Наименование", help_text="Наименование продукта",
    )
    description = models.TextField(
        verbose_name="Описание", help_text="Описание категории", null=True, blank=True,
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
    )
    description = models.TextField(
        verbose_name="Описание",
        null=True,
        blank=True,
    )
    image = models.ImageField(
        upload_to="products/",
        verbose_name="Изображение(превью)",
        null=True,
        blank=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        null=True,
        blank=True,
        related_name="products",
    )
    purchase_price = models.IntegerField(
        verbose_name="Цена за покупку",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания (записи в БД)",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата последнего изменения (записи в БД)",
    )
    author = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Автор', null=True, blank=True,
                               related_name='users',)

    sign_publication_product = models.BooleanField(default=False, verbose_name='Признак публикации продукта',)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

        # Кастомные команды для группы модераторов. Они могут: отменять публикацию продукта, менять описание любого
        # продукта и менять категорию любого продукта
        permissions = [
            ('may_cancel_publication_product', 'may cancel publication product'),
            ('can_change_description_product', 'can change description product'),
            ('can_change_category_product', 'can change category product')
        ]


class Version(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        verbose_name="Продукт",
        null=True,
        blank=True,
        related_name="products_version",
        )

    version_number = models.PositiveIntegerField(
        verbose_name='Номер версии',
        )

    version_name = models.CharField(
        max_length=50,
        verbose_name='Название версии',
        )

    indicates_current_version = models.BooleanField(
        default=False,
        verbose_name='Признак текущей версии',
        )

    def __str__(self):
        return f"{self.version_name} - {self.version_number}, {self.product}, {self.indicates_current_version}"

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"

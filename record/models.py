from django.db import models

from users.models import User


# Create your models here.

# Создание модели записей
class Records(models.Model):
    heading = models.CharField(max_length=50, verbose_name='заголовок')
    slug = models.CharField(max_length=100, verbose_name='slug', null=True, blank=True)
    content = models.TextField(verbose_name='содержимое')
    preview = models.ImageField(upload_to='records/', verbose_name='превью', null=True, blank=True)
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    sign_of_publication = models.BooleanField(default=True, verbose_name='признак публикации')
    number_of_views = models.IntegerField(default=0, verbose_name='количество просмотров')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Автор', null=True, blank=True,
                               related_name='author_users', )
    def __str__(self):
        return self.heading

    class Meta:
        verbose_name = 'блоговая запись'
        verbose_name_plural = 'блоговые записи'

        # Кастомная команда для группы контент-менеджеров. Они могут отменять публикацию продукта
        permissions = [
            ('may_cancel_publication_record', 'may cancel publication record')
        ]

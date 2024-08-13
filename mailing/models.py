from django.db import models


# Create your models here.
class Message(models.Model):
    """Модель сообщений для рассылки"""
    subject_of_letter = models.CharField(max_length=100, verbose_name="Тема письма")
    body_of_letter = models.TextField(verbose_name='Тело письма')

    def __str__(self):
        return self.subject_of_letter

    class Meta:
        verbose_name = "Сообщение для рассылки"
        verbose_name_plural = "Сообщения для рассылки"


class Customer(models.Model):
    """Модель клиента сервиса"""
    contact_email = models.EmailField(unique=True, verbose_name='Контактный email')
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    patronymic = models.CharField(max_length=50, verbose_name="Отчество")
    comment = models.TextField(verbose_name='Комментарий')

    def __str__(self):
        return f"{self.last_name} - {self.contact_email}"

    class Meta:
        verbose_name = "Клиент сервиса"
        verbose_name_plural = "Клиенты сервиса"


class Frequency(models.Model):
    """Модель периодичности рассылки"""
    name = models.CharField(max_length=20, verbose_name="Периодичность рассылки")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Периодичность рассылки"
        verbose_name_plural = "Периодичности рассылок"


class Mailing(models.Model):
    """Модель рассылки"""
    date_and_time_of_first_mailing = models.DateTimeField(null=True, blank=True,
                                                          verbose_name='дата и время первой отправки рассылки')
    frequency = models.ForeignKey(Frequency, on_delete=models.SET_NULL, verbose_name="Периодичность рассылки",
                                  related_name="frequency_of_mailing", null=True, blank=True)
    mailing_status = models.CharField(max_length=20, default='создана', verbose_name='Статус рассылки')
    message = models.ForeignKey(Message, on_delete=models.SET_NULL, verbose_name="Сообщение рассылки",
                                related_name="mailing_list_message", null=True, blank=True)
    customers_of_service = models.ManyToManyField(Customer, verbose_name="Пользователи сервиса",
                                                  related_name="customers_of_service")

    def __str__(self):
        return self.frequency

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"

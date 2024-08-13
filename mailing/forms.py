from django.forms import ModelForm

from catalog.forms import StyleFormMixin
from mailing.models import Message, Customer


class MessageForm(StyleFormMixin, ModelForm):
    """Класс форма для сообщений для рассылки"""
    class Meta:
        model = Message
        fields = '__all__'


class CustomerForm(StyleFormMixin, ModelForm):
    """Класс форма для клиентов сервиса"""
    class Meta:
        model = Customer
        fields = '__all__'

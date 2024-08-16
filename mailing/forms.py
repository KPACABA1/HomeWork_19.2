from django.forms import ModelForm

from catalog.forms import StyleFormMixin
from mailing.models import Message, Customer, Mailing


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


class MailingForm(StyleFormMixin, ModelForm):
    """Класс форма для рассылок"""
    class Meta:
        model = Mailing
        exclude = ('date_and_time_of_first_mailing', 'mailing_status')

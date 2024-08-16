from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from mailing.forms import MessageForm, CustomerForm, MailingForm
from mailing.models import Message, Customer, Mailing


# Create your views here.

class MessageListView(ListView):
    """Класс-контроллер для вывода всех сообщений"""
    model = Message
    template_name = 'mailing/message_list.html'


class MessageCreateView(CreateView):
    """Класс контроллер для создания сообщений для рассылки"""
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message_list')
    template_name = 'mailing/message_form.html'


class MessageUpdateView(UpdateView):
    """Класс контролер для редактирования сообщения для рассылки"""
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message_list')
    template_name = 'mailing/message_form.html'


class MessageDetailView(DetailView):
    """Класс-контроллер для вывода информации о сообщении для рассылки"""
    model = Message


class MessageDeleteView(DeleteView):
    """Класс-контроллер для удаления сообщения для рассылки"""
    model = Message
    success_url = reverse_lazy('mailing:message_list')


class CustomerListView(ListView):
    """Класс-контроллер для вывода всех клиентов сервиса"""
    model = Customer


class CustomerCreateView(CreateView):
    """Класс контроллер для создания клиентов сервиса"""
    model = Customer
    form_class = CustomerForm
    success_url = reverse_lazy('mailing:customer_list')


class CustomerUpdateView(UpdateView):
    """Класс контролер для редактирования клиентов сервиса"""
    model = Customer
    form_class = CustomerForm
    success_url = reverse_lazy('mailing:customer_list')


class CustomerDetailView(DetailView):
    """Класс-контроллер для вывода информации о клиентах сервиса"""
    model = Customer


class CustomerDeleteView(DeleteView):
    """Класс-контроллер для удаления клиента сервиса"""
    model = Customer
    success_url = reverse_lazy('mailing:customer_list')


class MailingListView(ListView):
    """Класс-контроллер для вывода всех рассылок"""
    model = Mailing


class MailingCreateView(CreateView):
    """Класс контроллер для создания рассылок"""
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailing_list')


class MailingUpdateView(UpdateView):
    """Класс контролер для редактирования рассылок"""
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailing_list')


class MailingDetailView(DetailView):
    """Класс-контроллер для вывода информации о рассылке"""
    model = Mailing


class MailingDeleteView(DeleteView):
    """Класс-контроллер для удаления рассылки"""
    model = Mailing
    success_url = reverse_lazy('mailing:mailing_list')

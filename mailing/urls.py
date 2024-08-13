from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from mailing.apps import MailingConfig
from mailing.views import MessageListView, MessageCreateView, MessageUpdateView, MessageDetailView, MessageDeleteView, \
    CustomerListView, CustomerCreateView, CustomerUpdateView, CustomerDetailView, CustomerDeleteView

app_name = MailingConfig.name

urlpatterns = [
    # Урлы для сообщений для рассылки
    path('message/', MessageListView.as_view(), name='message_list'),
    path('create_message/', MessageCreateView.as_view(), name='message_create'),
    path('edit_message/<int:pk>/', MessageUpdateView.as_view(), name='edit_message'),
    path('info_message/<int:pk>/', MessageDetailView.as_view(), name='info_message'),
    path('delete_message/<int:pk>/', MessageDeleteView.as_view(), name='delete_message'),

    # Урлы для клиентов сервиса
    path('customer/', CustomerListView.as_view(), name='customer_list'),
    path('create_customer/', CustomerCreateView.as_view(), name='create_customer'),
    path('edit_customer/<int:pk>/', CustomerUpdateView.as_view(), name='edit_customer'),
    path('info_customer/<int:pk>/', CustomerDetailView.as_view(), name='info_customer'),
    path('delete_customer/<int:pk>/', CustomerDeleteView.as_view(), name='delete_customer'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

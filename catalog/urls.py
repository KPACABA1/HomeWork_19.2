from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import index, contacts, info_product

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('info_product/<int:pk>/', info_product, name='info_product'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.decorators.cache import cache_page, never_cache

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ContactsTemplateView, ProductDetailView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView, CategoryListView
from config.settings import CACHE_ENABLED, CACHE_ENABLED_ENTIRE_SITE

app_name = CatalogConfig.name

# Если включён просто кэш для определенных контроллеров и низкоуровневый
if CACHE_ENABLED:
    urlpatterns = [
        path('', ProductListView.as_view(), name='product_list'),
        path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
        path('info_product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='info_product'),
        path('create/', ProductCreateView.as_view(), name='product_create'),
        path('edit/<int:pk>/', ProductUpdateView.as_view(), name='edit'),
        path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
        path('category/', CategoryListView.as_view(), name='category_list'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Если включен кэш для всего сайта
elif CACHE_ENABLED_ENTIRE_SITE:
    urlpatterns = [
        path('', never_cache(ProductListView.as_view()), name='product_list'),
        path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
        path('info_product/<int:pk>/', ProductDetailView.as_view(), name='info_product'),
        path('create/', ProductCreateView.as_view(), name='product_create'),
        path('edit/<int:pk>/', ProductUpdateView.as_view(), name='edit'),
        path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
        path('category/', CategoryListView.as_view(), name='category_list'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Если кэш выключен
else:
    urlpatterns = [
        path('', ProductListView.as_view(), name='product_list'),
        path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
        path('info_product/<int:pk>/', ProductDetailView.as_view(), name='info_product'),
        path('create/', ProductCreateView.as_view(), name='product_create'),
        path('edit/<int:pk>/', ProductUpdateView.as_view(), name='edit'),
        path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
        path('category/', CategoryListView.as_view(), name='category_list'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

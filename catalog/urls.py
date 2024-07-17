from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ContactsTemplateView, ProductDetailView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    path('info_product/<int:pk>/', ProductDetailView.as_view(), name='info_product'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

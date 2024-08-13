from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.decorators.cache import never_cache

from config.settings import CACHE_ENABLED_ENTIRE_SITE
from record.apps import RecordConfig
from record.views import RecordListView, RecordDetailView, RecordCreateView, RecordUpdateView, RecordDeleteView

app_name = RecordConfig.name

# Если включено кэширование всего сайта
if CACHE_ENABLED_ENTIRE_SITE:
    urlpatterns = [
        path('list/', never_cache(RecordListView.as_view()), name='record_list'),
        path('view/<int:pk>/', RecordDetailView.as_view(), name='view'),
        path('create/', RecordCreateView.as_view(), name='record_create'),
        path('edit/<int:pk>/', RecordUpdateView.as_view(), name='edit'),
        path('delete/<int:pk>/', RecordDeleteView.as_view(), name='delete'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Если кэширование всего сайта отключено
else:
    urlpatterns = [
            path('list/', RecordListView.as_view(), name='record_list'),
            path('view/<int:pk>/', RecordDetailView.as_view(), name='view'),
            path('create/', RecordCreateView.as_view(), name='record_create'),
            path('edit/<int:pk>/', RecordUpdateView.as_view(), name='edit'),
            path('delete/<int:pk>/', RecordDeleteView.as_view(), name='delete'),
        ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

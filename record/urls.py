from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from record.apps import RecordConfig
from record.views import RecordListView, RecordDetailView, RecordCreateView, RecordUpdateView, RecordDeleteView

app_name = RecordConfig.name

urlpatterns = [
    path('list/', RecordListView.as_view(), name='record_list'),
    path('view/<int:pk>/', RecordDetailView.as_view(), name='view'),
    path('create/', RecordCreateView.as_view(), name='record_create'),
    path('edit/<int:pk>/', RecordUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', RecordDeleteView.as_view(), name='delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
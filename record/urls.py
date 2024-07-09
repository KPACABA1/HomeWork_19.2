from django.urls import path
from record.apps import RecordConfig
from record.views import RecordListView, RecordDetailView, RecordCreateView, RecordUpdateView, RecordDeleteView

app_name = RecordConfig.name

urlpatterns = [
    path('list/', RecordListView.as_view(), name='record_list'),
    # path('detail/<int:pk>/', RecordDetailView.as_view(), name='detail'),
    path('create/', RecordCreateView.as_view(), name='record_create'),
    # path('update/<int:pk>/', RecordUpdateView.as_view(), name='update'),
    # path('delete/<int:pk>/', RecordDeleteView.as_view(), name='delete'),
]
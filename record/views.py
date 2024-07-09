from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from record.models import Records


# Класс-контроллер для вывода всех записей
class RecordListView(ListView):
    model = Records


# Класс-контроллер для детального просмотра записи
class RecordDetailView(DetailView):
    model = Records


# Класс-контроллер для создания записи
class RecordCreateView(CreateView):
    model = Records
    fields = ('heading', 'content',)
    success_url = reverse_lazy('catalog:product_list')


# Класс-контроллер для редактирования записи
class RecordUpdateView(UpdateView):
    model = Records


# Класс-контроллер для удаления записи
class RecordDeleteView(DeleteView):
    model = Records

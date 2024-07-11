from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from record.models import Records

from django.core.mail import send_mail



# Класс-контроллер для вывода всех записей
class RecordListView(ListView):
    model = Records

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(sign_of_publication=True)
        return queryset


# Класс-контроллер для детального просмотра записи
class RecordDetailView(DetailView):
    model = Records

    @staticmethod
    def send_mail():
        send_mail(subject='Тема письма',
            message='Ваша статья достигла 100 просмотров!',
            from_email="Ваша_почта",
            recipient_list=["Ваша_почта"],
        )

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.number_of_views += 1
        self.object.save()

        if self.object.number_of_views >= 100:
            self.send_mail()
        return self.object


# Класс-контроллер для создания записи
class RecordCreateView(CreateView):
    model = Records
    fields = ('heading', 'content', 'preview',)
    success_url = reverse_lazy('record:record_list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.heading)
            new_mat.save()
        return super().form_valid(form)


# Класс-контроллер для редактирования записи
class RecordUpdateView(UpdateView):
    model = Records
    fields = ('heading', 'content', 'preview',)
    success_url = reverse_lazy('record:record_list')

    def get_success_url(self):
        return reverse('record:view', args=[self.kwargs.get('pk')])


# Класс-контроллер для удаления записи
class RecordDeleteView(DeleteView):
    model = Records
    success_url = reverse_lazy('record:record_list')

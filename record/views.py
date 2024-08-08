from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from record.forms import RecordForm, RecordContentManagerForm
from record.models import Records

from django.core.mail import send_mail

# Импортирую данные почты для отправки письма
from dotenv import load_dotenv
import os

load_dotenv()


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
        """Метод для рассылки письма когда блоговая запись набрала 100+ просмотров"""
        send_mail(subject='Тема письма',
                  message='Ваша статья достигла 100 просмотров!',
                  from_email=os.getenv('mail'),
                  recipient_list=[os.getenv('mail')],
                  )

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.number_of_views += 1
        self.object.save(update_fields=['number_of_views'])

        if self.object.number_of_views >= 100:
            self.send_mail()
        return self.object


# Класс-контроллер для создания записи
class RecordCreateView(CreateView):
    model = Records
    fields = ('heading', 'content', 'preview')
    success_url = reverse_lazy('record:record_list')

    def form_valid(self, form):
        """Метод, который при создании записи авторизованным пользователем сразу присваивает этой записи его имя и
        присваивает ей slug"""
        if form.is_valid():
            new_mat = form.save()

            # Создаю slug
            new_mat.slug = slugify(new_mat.heading)

            # Присваиваю записи имя её автора
            user = self.request.user
            new_mat.author = user

            new_mat.save()
        return super().form_valid(form)


# Класс-контроллер для редактирования записи
class RecordUpdateView(LoginRequiredMixin, UpdateView):
    model = Records
    form_class = RecordForm
    success_url = reverse_lazy('record:record_list')

    def get_success_url(self):
        return reverse('record:view', args=[self.kwargs.get('pk')])

    def get_form_class(self):
        user = self.request.user
        if user == self.object.author:
            return RecordForm
        if user.has_perm('record.may_cancel_publication_record'):
            return RecordContentManagerForm



# Класс-контроллер для удаления записи
class RecordDeleteView(DeleteView):
    model = Records
    success_url = reverse_lazy('record:record_list')

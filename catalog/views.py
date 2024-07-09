from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product


# Create your views here.

# Класс-контроллер для вывода главной страницы
class ProductListView(ListView):
    model = Product


# Класс-контроллер для вывода станицы с контактами
class ContactsTemplateView(TemplateView):
    template_name = 'contacts.html'

    # Метод получения информации со страницы контакты
    def post(self, request):
        if request.method == 'POST':
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            print(f'Имя -{name}, телефон - {phone}, сообщение - {message}')
        return render(request, 'contacts.html')


# Класс-контроллер для вывода информации об отдельном продукте
class ProductDetailView(DetailView):
    model = Product

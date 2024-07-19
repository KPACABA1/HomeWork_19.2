from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version


# Create your views here.
class ProductListView(ListView):
    """Класс-контроллер для вывода главной страницы"""
    model = Product

    def get_context_data(self, **kwargs):
        """Метод для вывода названия версии если она активна"""
        context_data = super().get_context_data(**kwargs)
        version = []
        version.extend(Version.objects.get(product='1'))
        version_name = version[0].version_name
        context_data['version'] = version_name
        return context_data


class ProductCreateView(CreateView):
    """Класс-контроллер для создания нового продукта"""
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')


class ProductDetailView(DetailView):
    """Класс-контроллер для вывода информации об отдельном продукте"""
    model = Product


class ProductUpdateView(UpdateView):
    """Класс-контроллер для редактирования продукта"""
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')


class ProductDeleteView(DeleteView):
    """Класс-контроллер для удаления продукта"""
    model = Product
    success_url = reverse_lazy('catalog:product_list')


class ContactsTemplateView(TemplateView):
    """Класс-контроллер для вывода станицы с контактами"""
    template_name = 'contacts.html'

    def post(self, request):
        """Метод получения информации со страницы контакты"""
        if request.method == 'POST':
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            print(f'Имя -{name}, телефон - {phone}, сообщение - {message}')
        return render(request, 'contacts.html')

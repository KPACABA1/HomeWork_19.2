from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm
from catalog.models import Product, Version


# Create your views here.

# Класс-контроллер для вывода главной страницы
class ProductListView(ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        a = inlineformset_factory(Product, Version)
        context_data['formset'] = a()
        return context_data


# Класс-контроллер для создания нового продукта
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')


# Класс-контроллер для вывода информации об отдельном продукте
class ProductDetailView(DetailView):
    model = Product


# Класс-контроллер для редактирования продукта
class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')


# Класс-контроллер для удаления продукта
class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')


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

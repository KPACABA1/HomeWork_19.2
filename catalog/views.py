from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version


# Create your views here.

# Класс-контроллер для вывода главной страницы
class ProductListView(ListView):
    model = Product

    # def get_queryset(self):
    #     a = super().get_queryset()
    #     Product.version = a
    #     return Product.version

    # Метод для вывода названия версии если она активна
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        version = []
        version.append(Version.objects.get(product='1'))
        version_name = version[0].version_name
        context_data['version'] = version_name
        return context_data



# Класс-контроллер для создания нового продукта
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        formset = inlineformset_factory(Product, Version, VersionForm, extra=1)
        context_data['formset'] = formset()
        return context_data


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

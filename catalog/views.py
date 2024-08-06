from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm, ProductModeratorForm
from catalog.models import Product, Version


# Create your views here.
class ProductListView(ListView):
    """Класс-контроллер для вывода главной страницы"""
    model = Product

    def get_context_data(self, **kwargs):
        """Метод для вывода названия версии если она активна"""
        context_data = super().get_context_data(**kwargs)
        version_dict = {}
        # Запускаю цикл по моделям Product и сразу запускаю цикл по моделям Version, далее алгоритм проверят что модель
        # Version активная и если он видит что она привязана к продукту, то добавляет в словарь номер продукта и его
        # активную версию
        for product in Product.objects.all():
            for version in Version.objects.all():
                if version.indicates_current_version:
                    if version.product_id == int(product.pk):
                        version_dict[version.product_id] = version.version_name
        context_data['versions'] = version_dict
        return context_data


class ProductCreateView(LoginRequiredMixin, CreateView):
    """Класс-контроллер для создания нового продукта с ограничением на неавторизованных пользователей"""
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    # Настройки для работы LoginRequiredMixin, если пользователь не авторизованы его перекинет на страницу входа
    login_url = "/user/login/"
    redirect_field_name = "/"

    def form_valid(self, form):
        """Метод, который при создании записи авторизованным пользователем сразу присваивает этой записи его имя"""
        product = form.save()
        user = self.request.user
        product.author = user
        product.save()
        return super().form_valid(form)


class ProductDetailView(DetailView):
    """Класс-контроллер для вывода информации об отдельном продукте"""
    model = Product


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """Класс-контроллер для редактирования продукта с ограничением на неавторизованных пользователей"""
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    # Настройки для работы LoginRequiredMixin, если пользователь не авторизован его перекинет на страницу входа
    login_url = "/user/login/"
    redirect_field_name = "/"

    def get_context_data(self, **kwargs):
        """Метод для вывода формы версии при редактировании продукта"""
        context_data = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(Product, Version, VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = ProductFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = ProductFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        """Метод для сохранения формы при редактировании"""
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)

    def get_form_class(self):
        """Метод для определения какую форму использовать при редактировании продукта в зависимости от прав доступа"""

        # Получаю данные о пользователе
        user = self.request.user

        # Если пользователь владелец, то он может редактировать свой продукт в максимальном объеме
        if user == self.object.author:
            return ProductForm

        # Если пользователь модератор, то он может редактировать продукт в соответствии со своими полномочиями
        if user.has_perm('catalog.may_cancel_publication_product') and user.has_perm('catalog.can_change_description_product') and user.has_perm('catalog.can_change_category_product'):
            return ProductModeratorForm

        # Если нет никаких прав на изменение данного продукта, то вызываем ошибку
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """Класс-контроллер для удаления продукта с ограничением на неавторизованных пользователей"""
    model = Product
    success_url = reverse_lazy('catalog:product_list')

    # Настройки для работы LoginRequiredMixin, если пользователь не авторизован его перекинет на страницу входа
    login_url = "/user/login/"
    redirect_field_name = "/"


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

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from catalog.models import Product


# Create your views here.

# Класс-контроллер для вывода главной страницы
class ProductListView(ListView):
    model = Product


# Функция контроллер для вывода страницы с контактами
def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Имя -{name}, телефон - {phone}, сообщение - {message}')
    return render(request, 'contacts.html')


# Класс-контроллер для вывода информации об отдельном продукте
class ProductDetailView(DetailView):
    model = Product

# def info_product(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {'catalog': product}
#     return render(request, 'product_detail.html', context)

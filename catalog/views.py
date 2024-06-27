from django.shortcuts import render, get_object_or_404

from catalog.models import Product


# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'index.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Имя -{name}, телефон - {phone}, сообщение - {message}')
    return render(request, 'contacts.html')

def info_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'info_product.html', context)

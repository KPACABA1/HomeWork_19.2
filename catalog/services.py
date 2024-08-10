from django.core.cache import cache

from catalog.models import Product, Category
from config.settings import CACHE_ENABLED


def get_products_from_cache():
    """Сервисный слой для получения кэша в ProductListView"""
    # Если кэш активен, то начинаем работу с ним
    if CACHE_ENABLED:
        key = 'product_list'
        products_list_cache = cache.get(key)
        # Проверяю, получил ли я кэш
        if products_list_cache is not None:
            return products_list_cache
        # Если кэш не получен, то записываю его из БД для последующего использования
        else:
            products = Product.objects.all()
            cache.set(products, key)
            return products
    # Если кэш неактивен, то просто возвращаю все продукты
    else:
        return Product.objects.all()


def get_category_from_cache():
    """Сервисный слой для получения кэша в ProductListView"""
    # Если кэш активен, то начинаем работу с ним
    if CACHE_ENABLED:
        key = 'category_list'
        category_list_cache = cache.get(key)
        # Проверяю, получил ли я кэш
        if category_list_cache is not None:
            return category_list_cache
        # Если кэш не получен, то записываю его из БД для последующего использования
        else:
            category = Category.objects.all()
            cache.set(category, key)
            return category
    # Если кэш неактивен, то просто возвращаю все продукты
    else:
        return Category.objects.all()

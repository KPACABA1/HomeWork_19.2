import psycopg2
from django.core.management import BaseCommand

import json

from catalog.models import Category, Product

# Импортирую данные для входа в базу данных
from dotenv import load_dotenv
import os
load_dotenv()


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Создаю подключение к базе данных
        with psycopg2.connect(database=os.getenv('name_database'), user=os.getenv('user_database'),
                              password=os.getenv('password_database')) as conn:
            with conn.cursor() as cur:

                # Удаляю данные из таблицы Category и Product
                cur.execute('TRUNCATE TABLE catalog_product RESTART IDENTITY')
                conn.commit()
                cur.execute('TRUNCATE TABLE catalog_category RESTART IDENTITY CASCADE')
                conn.commit()

        # открываю соединение с файлом, в котором находятся все данные о категориях и продуктах
        with open('catalog.json', 'r', encoding='utf-8') as info_json:
            info_python = json.load(info_json)

            # создаю категории
            category_fill = []
            product_fill = []
            for c in info_python:
                if c['model'] == 'catalog.category':
                    category_fill.append(Category(**c['fields']))
            Category.objects.bulk_create(category_fill)

            # Создаю продукты
            id_ = 1
            for c in info_python:
                if c['model'] == 'catalog.product':
                    i = {'id': id_, 'name': c['fields']['name'], 'description': c['fields']['description'],
                            'image': c['fields']['image'], 'purchase_price': c['fields']['purchase_price'],
                            'created_at': c['fields']['created_at'], 'updated_at': c['fields']['updated_at'],
                            'category': Category.objects.get(pk=c['fields']['category'])}
                    id_ += 1
                    product_fill.append(Product(**i))
            Product.objects.bulk_create(product_fill)

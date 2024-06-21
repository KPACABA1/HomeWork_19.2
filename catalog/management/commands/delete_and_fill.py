import psycopg2
from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Не знаю надо или нет, но создаю подключение к базе данных
        with psycopg2.connect(database='homework_20_1', user='postgres', password='mr34mr58') as conn:
            with conn.cursor() as cur:
                # Вывожу и записываю данные из Category
                cur.execute('SELECT * FROM catalog_category')
                category_from_db = cur.fetchall()

                # Вывожу и записываю данные из Product
                cur.execute('SELECT * FROM catalog_product')
                product_from_db = cur.fetchall()

                # Удаляю данные из таблицы Category и Product
                cur.execute('TRUNCATE TABLE catalog_product RESTART IDENTITY')
                conn.commit()
                cur.execute('TRUNCATE TABLE catalog_category RESTART IDENTITY CASCADE')
                conn.commit()

                # Переделываю данные в список и заношу их в таблицу Category
                category_fill = []
                for category in category_from_db:
                    i = {'id': category[0], 'name': category[1], 'description': category[2]}
                    category_fill.append(Category(**i))
                Category.objects.bulk_create(category_fill)

                # Переделываю данные в список и заношу их в таблицу Product
                product_fill = []
                for product in product_from_db:
                    print(product[7])
                    i = {'id': product[0], 'name': product[1], 'description': product[2], 'image': product[3],
                         'purchase_price': product[4], 'created_at': product[5], 'updated_at': product[6],
                         'category': product[7]}
                    product_fill.append(Product(**i))
                Product.objects.bulk_create(product_fill)
        conn.close()

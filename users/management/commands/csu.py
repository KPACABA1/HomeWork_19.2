from django.core.management import BaseCommand

# Импортирую свою почту и свой пароль
from env.data import mail, password_database

from users.models import User


class Command(BaseCommand):
    """Кастомная команда для создания админа"""
    def handle(self, *args, **options):
        """Соответственно метод лдя создания админа где как почту использую свою почту и пароль написанные в env"""
        user = User.objects.create(email=mail, phone_number='89655427800')
        user.set_password(password_database)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()

from django.core.management import BaseCommand

# Импортирую свою почту, пароль и номер телефона
from dotenv import load_dotenv
import os

load_dotenv()

from users.models import User


class Command(BaseCommand):
    """Кастомная команда для создания админа"""

    def handle(self, *args, **options):
        """Соответственно метод лдя создания админа где как почту использую свою почту и пароль написанные в env"""
        user = User.objects.create(email=os.getenv('mail'), phone_number=os.getenv('phone_number'))
        user.set_password(os.getenv('password_database'))
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()

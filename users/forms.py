from django.contrib.auth.forms import UserCreationForm

from catalog.forms import StyleFormMixin
from users.models import User


class UsersRegisterForm(StyleFormMixin, UserCreationForm):
    """Класс форма для регистрации пользователей"""
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',)

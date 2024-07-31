from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from catalog.forms import StyleFormMixin
from users.models import User


class UsersRegisterForm(StyleFormMixin, UserCreationForm):
    """Класс форма для регистрации пользователей"""
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',)


class EditingProfileForm(UserChangeForm):
    """Форма для редактирования профиля пользователя"""
    class Meta:
        model = User
        fields = ('email', 'avatar', 'phone_number', 'country')

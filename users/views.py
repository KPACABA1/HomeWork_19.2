import random
import string

from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView, UpdateView

from env.data import mail
from users.forms import UsersRegisterForm, EditingProfileForm
from users.models import User

# Импортирую библиотеку секретов
import secrets


# Create your views here.
class UserCreateView(CreateView):
    """Класс-контроллер для регистрации пользователя"""
    model = User
    form_class = UsersRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """Метод для верификации пользователя по почте. Когда пользователь регистрируется, он становится не активным
        и ему надо подтвердить почту"""
        # Сделал пользователя не активным
        user = form.save()
        user.is_active = False
        # Генерирую код подтверждения
        token = secrets.token_hex(16)
        # Присваиваю пользователю токен
        user.token = token
        user.save()
        # Узнаю откуда пришёл пользователь
        host = self.request.get_host()
        url = f'http://{host}/user/email-confirm/{token}/'
        # Отправляю письмо с подтверждением
        send_mail(subject='Подтверждение почты',
                  message=f'Здравствуйте, чтобы подтвердить свою почту перейдите по ссылке {url}',
                  # Импортирую свою почту из env
                  from_email=mail,
                  recipient_list=[user.email],)
        return super().form_valid(form)


def email_verification(request, token):
    """Метод для того случая, когда пользователь подтвердил свою почту"""
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))


class ResetTemplateView(TemplateView):
    """Класс-контроллер для вывода станицы с контактами"""
    template_name = 'user_forgot_password.html'

    def password_generation(self, length):
        """Метод для генерации случайного пароля"""
        return ''.join(
            random.choices(
                string.ascii_letters + string.digits,
                k=length
            )
        )

    def post(self, request):
        """Метод сброса пароля в случае если пользователь его забыл"""
        # Если пользователь напишет свою почту и нажмет на кнопку отправить я узнаю его почту
        if request.method == 'POST':
            email = request.POST.get('email')

            # Нахожу пользователя по его почте
            user = User.objects.get(email=email)

            # Генерирую новый пароль
            new_password = self.password_generation(10)

            # Меняю пароль пользователю в базе данных
            user.set_password(new_password)
            user.save()

            # Узнаю откуда пришёл пользователь
            host = self.request.get_host()
            # Отправляю письмо с подтверждением
            send_mail(subject=f'Изменение пароля от почты {email}',
                      message=f'Здравствуйте, ваш новый пароль - {new_password}',
                      # Импортирую свою почту из env
                      from_email=mail,
                      recipient_list=[email], )
        return render(request, 'contacts.html')


class ProfileView(UpdateView):
    """Класс для редактирования профиля пользователя"""
    model = User
    form_class = EditingProfileForm
    success_url = reverse_lazy('users:profile')
    template_name = 'users/editing_profile.html'

    def get_object(self, queryset=None):
        """Метод для определения какому пользователю мы будем редактировать профиль"""
        return self.request.user

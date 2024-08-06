from django.forms import ModelForm, forms, BooleanField

from catalog.models import Product, Version


class StyleFormMixin:
    """Класс для стилизации форм"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = "form-check-input"
            else:
                field.widget.attrs['class'] = "form-control"


class ProductForm(StyleFormMixin, ModelForm):
    """Класс форма для продуктов"""
    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at', 'author', 'sign_publication_product')

    def clean_name(self):
        """Метод для фильтрации названия продукта от запрещённых слов"""
        cleaned_data = self.cleaned_data['name']

        # Кортеж запрещенных слов
        forbidden_words = ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар')

        # Проверю есть ли в названии запрещенные слова
        if cleaned_data in forbidden_words:
            raise forms.ValidationError('В названии продукта есть запрещённое слово')

        return cleaned_data

    def clean_description(self):
        """Метод для фильтрации описания продукта от запрещённых слов"""
        cleaned_data = self.cleaned_data['description']

        # Кортеж запрещенных слов
        forbidden_words = ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар')

        # Проверю есть ли в названии запрещенные слова
        if cleaned_data in forbidden_words:
            raise forms.ValidationError('В описании продукта есть запрещённое слово')

        return cleaned_data


class ProductModeratorForm(StyleFormMixin, ModelForm):
    """Класс форма для группы модераторов продуктов"""
    class Meta:
        model = Product
        fields = ('sign_publication_product', 'description', 'category',)

    def clean_description(self):
        """Метод для того, чтобы модератор при изменении описания продукта не добавил в него запрещённые слова"""
        cleaned_data = self.cleaned_data['description']

        # Кортеж запрещенных слов
        forbidden_words = ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар')

        # Проверю есть ли в названии запрещенные слова
        if cleaned_data in forbidden_words:
            raise forms.ValidationError('В описании продукта есть запрещённое слово')

        return cleaned_data


class VersionForm(StyleFormMixin, ModelForm):
    """Класс форма для версий"""
    class Meta:
        model = Version
        fields = '__all__'

    def clean(self):
        """Клин метод для проверки того, что при редактировании продукта пользователь выбрал активной версией только
        одну версию"""
        cleaned_data = super().clean()
        # получаем из формы значение поля indicates_current_version
        indicates_current_version = cleaned_data.get('indicates_current_version')
        # получаем связанный продукт версии
        product = self.instance.product

        # Проверяем была ли активна другая версия и если она была активна, то вызываем ошибку
        if indicates_current_version:
            if Version.objects.filter(product=product, indicates_current_version=True).exists():
                raise forms.ValidationError(cleaned_data)
        return cleaned_data

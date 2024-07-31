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
        exclude = ('created_at', 'updated_at', 'author')

    def clean_name(self):
        """Метод для фильтрования слов"""
        cleaned_data = self.cleaned_data['name']

        # Кортеж запрещенных слов
        forbidden_words = ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар')

        # Проверю есть ли в названии запрещенные слова
        if cleaned_data in forbidden_words:
            raise forms.ValidationError('В названии продукта есть запрещённое слово')

        return cleaned_data

    def clean_description(self):
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

    # def clean(self):
    #     """Клин метод для проверки того, что при редактировании продукта пользователь выбрал активной версией только
    #     одну версию"""
    #     cleaned_data = super().clean()
    #     # получаем из формы значение поля indicates_current_version
    #     indicates_current_version = cleaned_data.get('indicates_current_version')
    #     # поулчаем связанный продукт версии
    #     product = self.instance.product
    #
    #     if indicates_current_version:
    #         # Проверяем, есть ли уже активная версия
    #         if < существует версия, которая связана с продуктом и имеет признак активной версии >:
    #             raise forms.ValidationError(cleaned_data)
    #     return cleaned_data
    #
    #
    #     # cleaned_data = super().clean()
    #     # indicates_current_version = cleaned_data.get('indicates_current_version')
    #     # # product = self.instance.product
    #     # # if indicates_current_version:
    #     # #     if
    #     # print(indicates_current_version)
    #     # print('5555555555555')
    #
    #     return cleaned_data

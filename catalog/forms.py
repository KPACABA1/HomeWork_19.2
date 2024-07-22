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
        exclude = ('created_at', 'updated_at',)

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

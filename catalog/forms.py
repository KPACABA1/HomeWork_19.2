from django.forms import ModelForm, forms

from catalog.models import Product


# Форма для продукта
class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at',)

    # Метод для фильтрования слов
    def clean_name(self):
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

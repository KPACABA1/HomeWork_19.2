from django.forms import ModelForm

from catalog.forms import StyleFormMixin
from record.models import Records


class RecordForm(StyleFormMixin, ModelForm):
    """Класс форма для продуктов"""
    class Meta:
        model = Records
        exclude = ('slug', 'date_creation', 'sign_of_publication', 'number_of_views', 'author')


class RecordContentManagerForm(StyleFormMixin, ModelForm):
    """Класс форма для группы модераторов продуктов"""
    class Meta:
        model = Records
        fields = ('sign_of_publication',)

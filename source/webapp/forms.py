from django import forms
from django.forms import widgets
from webapp.models import STATUS_CHOIСES

class BookForm(forms.Form):
    name_author = forms.CharField(max_length=100, required=True, label='Имя автора', error_messages={'required': 'Поле обязательно для заполнения'}, help_text='Введите имя автора')
    email = forms.EmailField(max_length=50, required=True, label='Почта')
    text = forms.CharField(max_length=2000, required=True, label='Текст записи')
    # created_at = forms.DateTimeField(widget=widgets.DateTimeInput(attrs={"type": "date"}), label="Дата создания")
    # status = forms.ChoiceField(required=True, choices=STATUS_CHOIСES, label="Статус")

class BookDeleteForm(forms.Form):
    name_author = forms.CharField(max_length=100,
                            required=True,
                            label="Имя автора",
                            error_messages={"required": "Поле обязательно для заполнения"},
                            )
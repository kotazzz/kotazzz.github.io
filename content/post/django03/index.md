---
author: Kotaz
title: Django03. Работа с формами в Django
date: 2025-08-28 00:00:02
description: Создание и обработка форм в Django
categories: ["courses"]
tags: ["Python", "Django", "web", "forms"]
slug: django03
image: 00_placeholder.png
---

## Введение в формы Django

Формы в Django позволяют собирать и обрабатывать пользовательский ввод. Django предоставляет мощную систему форм, которая включает валидацию, рендеринг и обработку данных.

### Типы форм

- **Формы на основе моделей** (ModelForm) - автоматически генерируются из моделей
- **Обычные формы** (Form) - создаются вручную для произвольных данных

## Создание обычной формы

Создайте файл `forms.py` в вашем приложении:

```python
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Ваше имя')
    email = forms.EmailField(label='Email')
    message = forms.CharField(widget=forms.Textarea, label='Сообщение')
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('@example.com'):
            raise forms.ValidationError("Email должен быть с домена example.com")
        return email
```

### Поля формы

Основные типы полей:

- `CharField` - текстовое поле
- `EmailField` - поле для email
- `IntegerField` - целое число
- `DateField` - дата
- `BooleanField` - булево значение
- `ChoiceField` - поле выбора
- `FileField` - файл

### Виджеты

Виджеты определяют, как поле отображается в HTML:

```python
message = forms.CharField(
    widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}),
    label='Сообщение'
)
```

## Обработка форм в представлениях

### Функциональное представление

```python
from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Обработка данных
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Сохранить или отправить email
            return redirect('success')
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})
```

### Классовое представление

```python
from django.views.generic.edit import FormView
from .forms import ContactForm

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/success/'
    
    def form_valid(self, form):
        # Обработка валидных данных
        return super().form_valid(form)
```

## Шаблон для формы

```html
<!DOCTYPE html>
<html>
<head>
    <title>Контактная форма</title>
</head>
<body>
    <h1>Свяжитесь с нами</h1>
    
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Отправить</button>
    </form>
    
    <!-- Или ручной рендеринг -->
    <form method="post">
        {% csrf_token %}
        <div>
            {{ form.name.label_tag }}
            {{ form.name }}
            {% if form.name.errors %}
                <ul class="errors">
                    {% for error in form.name.errors %}
                        <li>{{ error }}</li>
                    {% endfor %}
                </ul>
            {% endif %}
        </div>
        <!-- Аналогично для других полей -->
        <button type="submit">Отправить</button>
    </form>
</body>
</html>
```

## ModelForm

Для создания форм на основе моделей:

```python
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'pub_date']
        widgets = {
            'pub_date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'title': 'Заголовок',
            'content': 'Содержание',
        }
```

### Использование ModelForm

```python
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = ArticleForm()
    
    return render(request, 'article_form.html', {'form': form})
```

## Валидация форм

### Встроенная валидация

Django автоматически проверяет:

- Обязательные поля
- Типы данных
- Максимальную длину
- Формат email

### Кастомная валидация

```python
def clean(self):
    cleaned_data = super().clean()
    start_date = cleaned_data.get('start_date')
    end_date = cleaned_data.get('end_date')
    
    if start_date and end_date and start_date > end_date:
        raise forms.ValidationError("Дата начала не может быть позже даты окончания")
    
    return cleaned_data
```

## Заключение

Формы Django предоставляют мощный и гибкий способ работы с пользовательским вводом. Они автоматически обрабатывают валидацию, рендеринг и защиту от CSRF-атак. Используйте ModelForm для форм, связанных с моделями, и обычные Form для произвольных данных.

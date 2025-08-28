---
author: Kotaz
title: Django02. Основы Django - Модели, Представления и Шаблоны
date: 2025-08-28 00:00:01
description: Создание приложений, моделей, представлений и шаблонов в Django
categories: ["courses"]
tags: ["Python", "Django", "web", "MTV"]
slug: django02
image: 00_placeholder.png
---

## Введение в MTV архитектуру

Django использует архитектуру MTV (Model-Template-View):

- **Model** - отвечает за данные и бизнес-логику
- **Template** - отвечает за представление данных
- **View** - обрабатывает запросы и возвращает ответы

## Создание приложения

1. Создайте новое приложение в проекте:

   ```bash
   python manage.py startapp myapp
   ```

2. Добавьте приложение в `settings.py`:

   ```python
   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
       'myapp',  # Добавьте эту строку
   ]
   ```

## Работа с моделями

Модели определяют структуру данных. Создайте модель в `myapp/models.py`:

```python
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title
```

### Миграции

1. Создайте миграцию:

   ```bash
   python manage.py makemigrations myapp
   ```

2. Примените миграцию:

   ```bash
   python manage.py migrate
   ```

## Представления (Views)

Представления обрабатывают запросы. Создайте в `myapp/views.py`:

```python
from django.shortcuts import render
from .models import Article

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'myapp/article_list.html', {'articles': articles})
```

## Маршрутизация URL

1. В `myapp/urls.py` (создайте файл):

   ```python
   from django.urls import path
   from . import views

   urlpatterns = [
       path('', views.article_list, name='article_list'),
   ]
   ```

2. В основном `urls.py` проекта:

   ```python
   from django.contrib import admin
   from django.urls import include, path

   urlpatterns = [
       path('admin/', admin.site.urls),
       path('articles/', include('myapp.urls')),
   ]
   ```

## Шаблоны (Templates)

Создайте директорию `myapp/templates/myapp/` и файл `article_list.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Список статей</title>
</head>
<body>
    <h1>Мои статьи</h1>
    <ul>
        {% for article in articles %}
        <li>
            <h2>{{ article.title }}</h2>
            <p>{{ article.content }}</p>
            <small>Опубликовано: {{ article.pub_date }}</small>
        </li>
        {% endfor %}
    </ul>
</body>
</html>
```

## Админ-панель

1. Создайте суперпользователя:

   ```bash
   python manage.py createsuperuser
   ```

2. Зарегистрируйте модель в `myapp/admin.py`:

   ```python
   from django.contrib import admin
   from .models import Article

   admin.site.register(Article)
   ```

3. Перейдите на [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) для доступа к админке.

## Заключение

Теперь вы знаете основы Django:

- Создание приложений
- Работа с моделями и миграциями
- Написание представлений
- Настройка URL-маршрутизации
- Создание шаблонов
- Использование админ-панели

Это базовый фундамент для разработки веб-приложений на Django. Продолжайте экспериментировать и изучать дополнительные возможности фреймворка!

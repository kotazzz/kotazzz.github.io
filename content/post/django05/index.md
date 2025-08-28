---
author: Kotaz
title: Django05. Работа с базами данных и ORM
date: 2025-08-28 00:00:04
description: Django ORM, запросы к базе данных и миграции
categories: ["courses"]
tags: ["Python", "Django", "web", "database", "ORM"]
slug: django05
image: 00_placeholder.png
---

## Введение в Django ORM

Django ORM (Object-Relational Mapping) - это система, которая позволяет работать с базами данных используя Python объекты вместо SQL запросов. ORM автоматически преобразует операции с объектами в SQL запросы.

### Поддерживаемые базы данных

Django поддерживает:

- PostgreSQL
- MySQL
- SQLite (по умолчанию)
- Oracle
- SQL Server

## Настройка базы данных

В `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```

## Создание моделей

Модели определяют структуру данных:

```python
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Article(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Черновик'),
        ('published', 'Опубликовано'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
```

### Типы полей

- `CharField` - строка
- `TextField` - длинный текст
- `IntegerField` - целое число
- `DecimalField` - десятичное число
- `BooleanField` - булево значение
- `DateTimeField` - дата и время
- `ForeignKey` - внешний ключ
- `ManyToManyField` - многие ко многим
- `OneToOneField` - один к одному

## Миграции

### Создание миграций

```bash
python manage.py makemigrations
python manage.py makemigrations myapp
```

### Применение миграций

```bash
python manage.py migrate
```

### Откат миграций

```bash
python manage.py migrate myapp 0001
```

## Основные запросы ORM

### Создание объектов

```python
# Создание и сохранение
category = Category(name='Python', slug='python')
category.save()

# Создание с помощью create()
article = Article.objects.create(
    title='Заголовок статьи',
    content='Содержание статьи',
    author=request.user,
    category=category
)
```

### Получение объектов

```python
# Получить все объекты
articles = Article.objects.all()

# Получить один объект
article = Article.objects.get(id=1)

# Получить или создать
article, created = Article.objects.get_or_create(
    title='Новая статья',
    defaults={'content': 'Содержание', 'author': request.user}
)

# Получить первое/последнее
first_article = Article.objects.first()
last_article = Article.objects.last()
```

### Фильтрация

```python
# Фильтр по полю
published_articles = Article.objects.filter(status='published')

# Исключение
draft_articles = Article.objects.exclude(status='published')

# Сложные условия
articles = Article.objects.filter(
    status='published',
    created_at__year=2023
)

# Поиск по тексту
articles = Article.objects.filter(title__icontains='python')

# Фильтр по связанным объектам
user_articles = Article.objects.filter(author__username='john')
```

### Операторы запросов

- `__exact` - точное совпадение
- `__icontains` - содержит (регистронезависимо)
- `__startswith` - начинается с
- `__endswith` - заканчивается на
- `__gt` - больше
- `__gte` - больше или равно
- `__lt` - меньше
- `__lte` - меньше или равно
- `__in` - в списке
- `__range` - в диапазоне
- `__year`, `__month`, `__day` - для дат

### Сортировка и ограничение

```python
# Сортировка
articles = Article.objects.order_by('-created_at')
articles = Article.objects.order_by('title', '-created_at')

# Ограничение количества
recent_articles = Article.objects.order_by('-created_at')[:5]

# Обратная сортировка
articles = Article.objects.order_by('-created_at').reverse()
```

### Агрегация и аннотация

```python
from django.db.models import Count, Sum, Avg, Max, Min

# Подсчет
total_articles = Article.objects.count()
category_count = Article.objects.values('category__name').annotate(count=Count('id'))

# Сумма, среднее и т.д.
from django.db.models import Sum
total_views = Article.objects.aggregate(Sum('views'))['views__sum']

# Аннотация
articles_with_comment_count = Article.objects.annotate(
    comment_count=Count('comments')
)
```

### Обновление объектов

```python
# Обновление одного объекта
article = Article.objects.get(id=1)
article.title = 'Новый заголовок'
article.save()

# Обновление нескольких объектов
Article.objects.filter(status='draft').update(status='published')

# Обновление с F-выражениями
from django.db.models import F
Article.objects.filter(id=1).update(views=F('views') + 1)
```

### Удаление объектов

```python
# Удаление одного объекта
article = Article.objects.get(id=1)
article.delete()

# Удаление нескольких объектов
Article.objects.filter(status='draft').delete()
```

## Работа со связанными объектами

### Foreign Key

```python
# Получение связанных объектов
article = Article.objects.get(id=1)
author = article.author  # Получить автора
category = article.category  # Получить категорию

# Обратная связь
user = User.objects.get(username='john')
user_articles = user.article_set.all()  # Все статьи пользователя
```

### Many-to-Many

```python
# Добавление связи
article.tags.add(tag1, tag2)

# Удаление связи
article.tags.remove(tag1)

# Установка связей
article.tags.set([tag1, tag3])

# Проверка связи
if article.tags.filter(name='python').exists():
    pass
```

### Предварительная загрузка (prefetch_related, select_related)

```python
# select_related для Foreign Key (один запрос)
articles = Article.objects.select_related('author', 'category').all()

# prefetch_related для Many-to-Many (два запроса)
articles = Article.objects.prefetch_related('tags').all()

# Комбинирование
articles = Article.objects.select_related('author').prefetch_related('tags').all()
```

## Raw SQL запросы

```python
from django.db import connection

# Raw SQL
articles = Article.objects.raw('SELECT * FROM myapp_article WHERE status = %s', ['published'])

# Прямой SQL
with connection.cursor() as cursor:
    cursor.execute("SELECT COUNT(*) FROM myapp_article")
    row = cursor.fetchone()
```

## Оптимизация запросов

### Использование индексов

```python
class Article(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    created_at = models.DateTimeField(db_index=True)
```

### Кеширование запросов

```python
from django.core.cache import cache

def get_popular_articles():
    cache_key = 'popular_articles'
    articles = cache.get(cache_key)
    
    if articles is None:
        articles = Article.objects.filter(status='published').order_by('-views')[:10]
        cache.set(cache_key, articles, 3600)  # Кеш на 1 час
    
    return articles
```

## Заключение

Django ORM предоставляет мощный и удобный интерфейс для работы с базами данных. Он позволяет писать меньше кода, автоматически генерирует SQL и предоставляет множество инструментов для оптимизации запросов. Понимание основных концепций ORM поможет вам эффективно работать с данными в Django проектах.

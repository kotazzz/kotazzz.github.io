---
author: Kotaz
title: Django04. Аутентификация и авторизация пользователей
date: 2025-08-28 00:00:03
description: Система аутентификации пользователей в Django
categories: ["courses"]
tags: ["Python", "Django", "web", "auth", "users"]
slug: django04
image: 00_placeholder.png
---

## Введение в систему аутентификации Django

Django предоставляет встроенную систему аутентификации, которая включает регистрацию, вход, выход и управление пользователями. Она основана на модели User и предоставляет готовые представления и формы.

### Основные компоненты

- **User модель** - стандартная модель пользователя
- **Authentication backends** - способы проверки учетных данных
- **Permissions** - система прав доступа
- **Groups** - группировка пользователей

## Настройка аутентификации

Убедитесь, что в `INSTALLED_APPS` есть:

```python
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    # ... другие приложения
]
```

## Работа с пользователями

### Создание пользователя

```python
from django.contrib.auth.models import User

# Создание пользователя
user = User.objects.create_user(
    username='john',
    email='john@example.com',
    password='password123'
)

# Создание суперпользователя
User.objects.create_superuser(
    username='admin',
    email='admin@example.com',
    password='admin123'
)
```

### Получение текущего пользователя

В представлениях:

```python
def my_view(request):
    current_user = request.user
    if current_user.is_authenticated:
        # Пользователь авторизован
        return render(request, 'user_page.html', {'user': current_user})
    else:
        # Пользователь не авторизован
        return redirect('login')
```

## Встроенные представления

Django предоставляет готовые представления для аутентификации:

### URLs для аутентификации

```python
from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
```

### Настройка шаблонов

Создайте шаблоны в `templates/registration/`:

`login.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Вход</title>
</head>
<body>
    <h1>Вход в систему</h1>
    
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Войти</button>
    </form>
    
    <p><a href="{% url 'password_reset' %}">Забыли пароль?</a></p>
</body>
</html>
```

## Кастомные формы аутентификации

### Форма регистрации

```python
from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label='Подтвердите пароль')
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
    
    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают')
        return password_confirm
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
```

### Представление регистрации

```python
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'register.html', {'form': form})
```

## Декораторы для защиты представлений

### @login_required

```python
from django.contrib.auth.decorators import login_required

@login_required
def protected_view(request):
    return render(request, 'protected.html')
```

### @user_passes_test

```python
from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return user.is_staff

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin.html')
```

## Система прав (Permissions)

### Создание прав

```python
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from myapp.models import Article

# Создание права
content_type = ContentType.objects.get_for_model(Article)
permission = Permission.objects.create(
    codename='can_publish',
    name='Can publish articles',
    content_type=content_type,
)
```

### Проверка прав

```python
def publish_article(request, article_id):
    article = Article.objects.get(id=article_id)
    
    if request.user.has_perm('myapp.can_publish'):
        article.published = True
        article.save()
        return redirect('article_detail', article_id)
    else:
        return render(request, 'no_permission.html')
```

### В шаблонах

```html
{% if perms.myapp.can_publish %}
    <a href="{% url 'publish_article' article.id %}">Опубликовать</a>
{% endif %}
```

## Группы пользователей

```python
from django.contrib.auth.models import Group

# Создание группы
editors_group = Group.objects.create(name='Editors')

# Добавление пользователя в группу
user.groups.add(editors_group)

# Проверка принадлежности к группе
if user.groups.filter(name='Editors').exists():
    # Пользователь в группе редакторов
    pass
```

## Кастомная модель пользователя

Для расширения модели User:

```python
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
```

Не забудьте указать в `settings.py`:

```python
AUTH_USER_MODEL = 'myapp.CustomUser'
```

## Заключение

Система аутентификации Django предоставляет все необходимое для управления пользователями. Она включает готовые представления, формы и декораторы, которые можно легко настроить под конкретные нужды проекта. Для сложных требований можно расширить стандартную модель User или создать полностью кастомную систему аутентификации.

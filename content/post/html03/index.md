---
author: Kotaz
title: "HTML Формы: Собираем данные от пользователей"
date: 2025-04-01 00:00:00
description: "Изучаем HTML формы: элементы, атрибуты и способы отправки данных на сервер."
categories: ["webdev"]
tags: ["HTML", "Forms", "Input", "Tutorial"]
slug: html03
image: 00_placeholder.png
---

## 📝 HTML Формы

HTML формы используются для сбора данных от пользователей. Форма состоит из различных элементов, таких как текстовые поля, кнопки, выпадающие списки и т.д.

### Основной тег `<form>`

Все элементы формы должны быть заключены в тег `<form>`.

Атрибут `action` указывает URL-адрес, на который будут отправлены данные формы.
Атрибут `method` определяет HTTP-метод, используемый для отправки данных (GET или POST).

Пример:

```html
<form action="/submit" method="post">
    <!-- Элементы формы -->
</form>
```

### Элементы формы

#### `<input>`

Тег `<input>` является наиболее распространенным элементом формы. Атрибут `type` определяет тип поля ввода.

Примеры:

- Текстовое поле: `<input type="text" name="username">`
- Пароль: `<input type="password" name="password">`
- Кнопка отправки: `<input type="submit" value="Отправить">`
- Чекбокс: `<input type="checkbox" name="agree">`
- Радиокнопка: `<input type="radio" name="gender" value="male">`

#### `<textarea>`

Тег `<textarea>` создает многострочное текстовое поле.

Пример:

```html
<textarea name="message" rows="5" cols="30"></textarea>
```

#### `<select>` и `<option>`

Тег `<select>` создает выпадающий список. Каждый элемент списка определяется тегом `<option>`.

Пример:

```html
<select name="country">
    <option value="usa">США</option>
    <option value="uk">Великобритания</option>
    <option value="canada">Канада</option>
</select>
```

#### `<button>`

Тег `<button>` создает кнопку.

Пример:

```html
<button type="submit">Отправить</button>
```

### Атрибуты элементов формы

- `name`: Определяет имя элемента формы (используется для отправки данных на сервер).
- `value`: Определяет значение элемента формы.
- `placeholder`: Отображает подсказку в текстовом поле.
- `required`: Указывает, что поле обязательно для заполнения.
- `readonly`: Указывает, что поле доступно только для чтения.
- `disabled`: Указывает, что поле отключено.

### Пример полной формы

```html
<form action="/submit" method="post">
    <label for="username">Имя пользователя:</label>
    <input type="text" id="username" name="username" required minlength="3" placeholder="Введите имя">

    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required placeholder="example@domain.com">

    <label for="password">Пароль:</label>
    <input type="password" id="password" name="password" required minlength="8">

    <label for="country">Страна:</label>
    <select id="country" name="country" required>
        <option value="">Выберите страну</option>
        <option value="ru">Россия</option>
        <option value="us">США</option>
        <option value="uk">Великобритания</option>
    </select>

    <button type="submit">Отправить</button>
</form>
```

## 🚀 Практическое задание

1. Создайте HTML-страницу с формой.
2. Добавьте различные элементы формы: текстовые поля, пароль, чекбоксы, радиокнопки, выпадающий список и кнопку отправки.
3. Установите атрибуты `name`, `value`, `placeholder` и `required` для элементов формы.
4. Проверьте, как отображается форма в браузере.

## 🎯 Следующие шаги

В следующих статьях мы рассмотрим, как стилизовать HTML формы с помощью CSS и как обрабатывать данные формы на сервере. Следите за обновлениями!

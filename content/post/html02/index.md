---
author: Kotaz
title: "HTML Списки и Ссылки: Углубляем знания"
date: 2025-04-02 00:00:00
description: "Изучаем HTML списки (упорядоченные и неупорядоченные) и ссылки, способы их создания и настройки."
categories: ["webdev"]
tags: ["HTML", "Lists", "Links", "Tutorial"]
slug: html02
image: 00_placeholder.png
---

## 📜 HTML Списки

HTML предлагает три типа списков:

1. Упорядоченные списки (`<ol>`) - элементы нумеруются.
2. Неупорядоченные списки (`<ul>`) - элементы маркируются.
3. Списки определений (`<dl>`) - элементы состоят из термина и его определения (не рассматриваем в этой статье).

### Упорядоченные списки

Используйте `<ol>`, чтобы создать упорядоченный список. Каждый элемент списка заключается в тег `<li>`.

Пример:

```html
<ol>
    <li>Первый элемент</li>
    <li>Второй элемент</li>
    <li>Третий элемент</li>
</ol>
```

### Неупорядоченные списки

Используйте `<ul>`, чтобы создать неупорядоченный список. Каждый элемент списка также заключается в тег `<li>`.

Пример:

```html
<ul>
    <li>Первый элемент</li>
    <li>Второй элемент</li>
    <li>Третий элемент</li>
</ul>
```

## 🔗 HTML Ссылки

HTML ссылки позволяют переходить с одной веб-страницы на другую. Ссылки создаются с помощью тега `<a>`.

Атрибут `href` указывает URL-адрес, на который ведет ссылка.

Пример:

```html
<a href="https://www.example.com">Посетите Example</a>
```

### Атрибут target

Атрибут `target` определяет, где будет открыта ссылка. Значение `_blank` открывает ссылку в новой вкладке или окне.

Пример:

```html
<a href="https://www.example.com" target="_blank">Посетите Example в новой вкладке</a>
```

### Ссылки на другие страницы вашего сайта

Чтобы создать ссылку на другую страницу вашего сайта, используйте относительный путь к этой странице.

Пример:

```html
<a href="/about">О нас</a>
```

## 🚀 Практическое задание

1. Создайте HTML-страницу.
2. Добавьте упорядоченный и неупорядоченный списки.
3. Добавьте несколько ссылок, ведущих на разные сайты и страницы вашего сайта.
4. Проверьте, как отображаются списки и работают ссылки в браузере.

## 🎯 Следующие шаги

В следующих статьях мы рассмотрим, как работать с изображениями и таблицами в HTML. Следите за обновлениями!

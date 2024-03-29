---
author: Kotaz
title: Py04. Инструкция if
date: 2022-07-23 03:00:00
description: Базовая информация по ветвлениям в Python
categories: ["courses"]
tags: ["Python"]
slug: py04
image: 00_placeholder.png
---


Условная инструкция if-elif-else (её ещё иногда называют оператором ветвления) - основной инструмент выбора в Python. Проще говоря, она выбирает, какое действие следует выполнить, в зависимости от значения переменных в момент проверки условия.

## Синтаксис `if`

Сначала записывается часть if с условным выражением, далее могут следовать одна или более необязательных частей elif, и, наконец, необязательная часть else. Общая форма записи условной инструкции if выглядит следующим образом:

```py
if test1:
    state1
elif test2:
    state2
else:
    state3
```

Простой пример (напечатает 'true', так как 1 - истина):

```py
>>> if 1:
...     print('true')
... else:
...     print('false')
...
true
```

Чуть более сложный пример (его результат будет зависеть от того, что ввёл пользователь):

```py
a = int(input())
if a < -5:
    print('Low')
elif -5 <= a <= 5:
    print('Mid')
else:
    print('High')
```

## Проверка истинности в Python

- Любое число, не равное 0, или непустой объект - истина.
- Числа, равные 0, пустые объекты и значение None - ложь
- Операции сравнения применяются к структурам данных рекурсивно
- Операции сравнения возвращают True или False
- Логические операторы and и or возвращают истинный или ложный объект-операнд

## Логические операторы

- `X and Y`: Истина, если оба значения X и Y истинны.
- `X or Y`: Истина, если хотя бы одно из значений X или Y истинно.
- `not X`: Истина, если X ложно.
- `X is Y`: Истина, если объект X является объектом Y.
- `X is not Y`: Истина, если объект X не является объектом Y.
- `X == Y`: Истина, если значения X и Y равны.
- `X != Y`: Истина, если значения X и Y не равны.
- `X > Y`: Истина, если значение X больше значения Y.
- `X >= Y`: Истина, если значение X больше или равно значению Y.
- `X < Y`: Истина, если значение X меньше значения Y.
- `X <= Y`: Истина, если значение X меньше или равно значению Y.

## Трехместное выражение if/else

Следующая инструкция:

```py
if X:
    A = Y
else:
    A = Z
```

довольно короткая, но, тем не менее, занимает целых 4 строки. Специально для таких случаев и было придумано выражение if/else:

```py
A = Y if X else Z
```

В данной инструкции интерпретатор выполнит выражение Y, если X истинно, в противном случае выполнится выражение Z.

```py
>>>
>>> A = 't' if 'spam' else 'f'
>>> A
't'
```

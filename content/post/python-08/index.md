---
author: Kotaz
title: Py08. zip() и enumerate()
date: 2023-02-28 05:00:00
description: zip() и enumerate() - полезные функции. Отлично сочетаются со списками. Разберем их поведение в этой статье
categories: ["courses"]
tags: ["Python"]
slug: py08
image: 00_placeholder.jpg
---

## Введение

Чтобы быть в состоянии понять приемы цикла for, нам нужно сначала знать, как присваивать значения нескольким переменным одновременно. Это работает следующим образом:

```python
>>> a, b = 1, 2
>>> a
1
>>> b
2
>>>
```

Мы можем использовать `()` и `[]` вокруг этих значений так, как мы хотим, и все по-прежнему будет работать таким же образом. `[]` создает список, а `()` создает кортеж.

```python
>>> [a, b] = (1, 2)
>>> a
1
>>> b
2
>>>
```

Мы также можем иметь `[]` или `()` на одной стороне, но не на другой стороне.

```python
>>> (a, b) = 1, 2
>>> a
1
>>> b
2
>>>
```

Python автоматически создал кортеж.

```python
>>> 1, 2
(1, 2)
>>>
```

Если мы зацикливаемся на списке с парами значений в нем, мы могли бы сделать это:

```python
>>> items = [('a', 1), ('b', 2), ('c', 3)]
>>> for pair in items:
...     a, b = pair
...     print(a, b)
...
a 1
b 2
c 3
>>>
```

Или мы можем сказать циклу for распаковать его для нас.

```python
>>> for a, b in items:
...     print(a, b)
...
a 1
b 2
c 3
>>>
```

Эта функция часто используется со встроенными в Python функциями `zip()` и `enumerate()`.

## zip

Что приходит вам на ум, когда вы слышите слово `молния`? Механизм, широко используемый для связывания двух частей чего-либо, например рубашки или пиджака. Функции Python `zip()` делают практически то же самое, это помогает нам связать соответствующие элементы вместе.

```python
>>> users = ["Tushar", "Aman", "Anurag", "Sohit"]
>>> uids = ["usr122", "usr123", "usr124", "usr125"]
>>> user_details = zip(uids, users)
>>> print(list(user_details))
[('usr122', 'Tushar'), ('usr123', 'Aman'), ('usr124', 'Anurag'), ('usr125', 'Sohit')]
>>>
```

Обратите внимание, что `print(user_details)` работает не так, как ожидалось:

```
>>> print(user_details)
<zip object at 0x0000016938E311C0>
>>>
```

Это потому, что `zip()` является итератором, то есть ленивым: он выдает элементы по мере необходимости, вместо того, чтобы вычислять их и сохранять в памяти все сразу, как список. Таким образом, объект zip не может показать свои элементы до того, как они будут использованы, потому что он их еще не вычислил.

```python
>>> users = ["Tushar", "Aman", "Anurag", "Sohit"]
>>> uids = ["usr122", "usr123", "usr124", "usr125"]
>>> user_details = zip(uids, users)
```

Если списки имеют разную длину, некоторые элементы из конца более длинного списка будут проигнорированы.

```python
>>> users = ["Tushar", "Aman", "Anurag"]
>>> emails = ["tushar@example.com", "aman@example.com", "anurag@example.com", "sohit@example.com"]
>>> users_contact = zip(users, emails)
>>> print(list(users_contact))
[('Tushar', 'tushar@example.com'), ('Aman', 'aman@example.com'), ('Anurag', 'anurag@example.com')]
>>>
```

Здесь самый короткий список - "пользователи" длиной 3, поэтому "zip (пользователи, электронные письма)" принимает только первые 3 электронных письма.
Мы не рекомендуем вызывать `zip()` со списками разной длины, потому что игнорирование элементов обычно не то, что вы намеревались делать.

### Использование zip в цикле `for`

Очень часто `for` зацикливается на `zip()` и распаковывает возвращенные кортежи в цикле `for`.
Вот почему мы представили распаковку в начале этой страницы.
При использовании таким образом нет необходимости преобразовывать результат `zip(...)` в список.

```python
>>> roll_nums = [20, 25, 28]
>>> students = ["Joe", "Max", "Michel"]
>>> for roll_num, student in zip(roll_nums, students):
...     print(f"Roll number of {student} is {roll_num}")
...
Roll number of Joe is 20
Roll number of Max is 25
Roll number of Michel is 28
>>>
```

## enumerate

`enumerate()` - это удивительная встроенная функция, предлагаемая python. При использовании дает нам объединенный индекс и элемент.

```python
>>> even_nums = [2, 4, 6, 8, 10, 12]
>>> for index, item in enumerate(even_nums):
...     print(f"Index of {item} is {index}")
...
Index of 2 is 0
Index of 4 is 1
Index of 6 is 2
Index of 8 is 3
Index of 10 is 4
Index of 12 is 5
>>>
```

Также возможно (но более сложно) сделать это без `enumerate()`:

```python
>>> even_nums = [2, 4, 6, 8, 10, 12]
>>> for index in range(0,  len(even_nums)):
...     print(f"Index of {even_nums[index]} is {index}")
...
Index of 2 is 0
Index of 4 is 1
Index of 6 is 2
Index of 8 is 3
Index of 10 is 4
Index of 12 is 5
>>>
```

Здесь:

* `range(0, len(even_nums))` дает 0,1,2,3,4,5, при этом длина списка 6 исключена. Это индексы нашего списка длиной 6.
* `even_nums[index]` выводит каждый элемент `even_nums`, потому что `index` берется из диапазона всех индексов в этом списке.

Поскольку об этом сложно думать и легко ошибиться, лучше использовать `enumerate()`.

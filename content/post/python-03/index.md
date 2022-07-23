---
author: Kotaz
title: Почему моя программа не работает? (FAQ)
date: 2022-07-23 02:00:00
description: FAQ по ошибкам
categories: ["courses"]
tags: ["Python"]
slug: py03
# image: 00_placeholder.jpg
---

# Почему моя программа не работает? (FAQ)

## Не работает функция `input`. Пишет `SyntaxError`

Пример кода:

```py
>>> a = input()
hello world
  File "<string>", line 1
    hello world
              ^
SyntaxError: unexpected EOF while parsing

```

**Причина:** Вы запустили Python 2.

**Решение:** Установить Python 3.

## Где-то увидел простую программу, а она не работает

Пример кода:

```py
name = raw_input()
print name
Ошибка:

  File "a.py", line 3
    print name
             ^
SyntaxError: invalid syntax
```

**Причина:** Вам подсунули программу на Python 2.

**Решение:** Прочитать об отличиях Python 2 от Python 3. Переписать её на Python 3. Например, данная программа на Python 3 будет выглядеть так:

```py
name = input()
print(name)
```

## `TypeError: Can't convert 'int' object to str implicitly`

Пример кода:

```py
>>> a = input() + 5
8
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Can't convert 'int' object to str implicitly
```

**Причина:** Нельзя складывать строку с числом.

**Решение:** Привести строку к числу с помощью функции int(). Кстати, заметьте, что функция input() всегда возвращает строку!

```py
>>>
>>> a = int(input()) + 5
8
>>> a
13
```

## `SyntaxError: invalid syntax`

Пример кода:

```py
>>> a = 5
>>> if a == 5
...     print('Ура!')
  File "a.py", line 3
    if a == 5
            ^
SyntaxError: invalid syntax
```

**Причина:** Забыто двоеточие.

**Решение:**

```py
a = 5
if a == 5:
    print('Ура!')
```

## `SyntaxError: invalid syntax` 2

Пример кода:

```py
>>> a = 5
>>> if a = 5:
...     print('Ура!')

  File "a.py", line 3
    if a = 5
         ^
SyntaxError: invalid syntax
```

**Причина:** Забыто равно.

**Решение:**

```py
a = 5
if a == 5:
    print('Ура!')
```

## `NameError: name 'a' is not defined`

Пример кода:

```py
print(a)
```

**Причина:** Переменная "a" не существует. Возможно, вы опечатались в названии или забыли инициализировать её.

**Решение:** Исправить опечатку.

```py
a = 10
print(a)
```

## `IndentationError: expected an indented block`

Пример кода:

```py
>>> a = 10
>>> if a > 0:
... print(a)
```

**Причина:** Нужен отступ.

**Решение:**

```py
a = 10
if a > 0:
    print(a)
```

## `TabError: inconsistent use of tabs and spaces in indentation`

Пример кода:

```py
>>> a = 10
>>> if a > 0:
...    print(a)
...    print('Ура!')
  File "a.py", line 5
    print('Ура!')
                 ^
TabError: inconsistent use of tabs and spaces in indentation
```

**Причина:** Смешение пробелов и табуляции в отступах.

**Решение:** Исправить отступы.

```py
a = 10
if a > 0:
    print(a)
    print('Ура!')
```

## `UnboundLocalError: local variable 'a' referenced before assignment`

Пример кода:

```py
def f():
    a += 1
    print(a)

a = 10
f()
```

```py
Traceback (most recent call last):
  File "a.py", line 7, in <module>
    f()
  File "a.py", line 3, in f
    a += 1
UnboundLocalError: local variable 'a' referenced before assignment
```

**Причина:** Попытка обратиться к локальной переменной, которая ещё не создана.

**Решение:**

```py
def f():
    global a
    a += 1
    print(a)

a = 10
f()
```

## Программа выполнилась, но в файл ничего не записалось / записалось не всё

Пример кода:

```py
>>>
>>> f = open('output.txt', 'w', encoding='utf-8')
>>> f.write('bla')
3
>>>
```

**Причина:** Не закрыт файл, часть данных могла остаться в буфере.

**Решение:**

```py
>>>
>>> f = open('output.txt', 'w', encoding='utf-8')
>>> f.write('bla')
3
>>> f.close()
>>>
```

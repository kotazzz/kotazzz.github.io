---
author: Kotaz
title: Py02. Основы Python
date: 2022-07-22 01:00:00
description: Познакомимся с переменными, вводом, выводом и типами
categories: ["courses"]
tags: ["Python"]
slug: py02
image: 00_placeholder.jpg
---

## Начало работы с языком

Сейчас большинство операций с кодом будет проводиться внутри файла. Если вы хотите повторить то, что происходит тут, создайте файл и пишите код туда. О том, как запустить файл, можно узнать в прошлом уроке.

## Вывод

### Вывод на экран

Выводимые данные можно перечислять через запятую

```py
print("Hello, world!") # Hello, world!
print("A", "B") # A B
print(1, 2, 3) # 1 2 3
print(True, False, None) # True False None
print("a", 1, True) # a 1 True
```

Так же можно проводить простые вычисления

```py
print(1 + 2) # 3
print(1 + 2, 3 + 4) # 3 7
print(1 - 3) # -2
```

### `sep =`

`sep` — это может быть строка, которую необходимо вставлять между значениями, по умолчанию — пробел.

Вставим список слов в print и разделим их с помощью символа новой строки. Еще раз: по умолчанию разделитель добавляет пробел между каждым словом.

```py
print('туториал', 'по', 'функции', 'print()')
# туториал по функции print()
```

`\n` перенесет каждое слово на новую строку

```py
print('туториал', 'по', 'функции', 'print()', sep='\n')
# туториал
# по
# функции
# print()
```

### `end =`

`end` — это строка, которая добавляется после последнего значения. По умолчанию — это перенос на новую строку (`\n`). С помощью аргумента end программист может самостоятельно определить окончание выражения print.

Предположим, есть две строки, а задача состоит в том, чтобы объединить их, оставив пробел. Для этого нужно в первой функции print указать первую строку, str1 и аргумент end с кавычками. В таком случае на экран выведутся две строки с пробелом между ними.

```py
str1 = 'туториал по'
str2 = 'функции print()'

print(str1)
print(str2)
# туториал по
# функции print()
print(str1, end=' ')
print(str2)
# туториал по функции print()
```

Возьмем другой пример, где есть функция, которая должна выводить значения списка на одной строке. Этого можно добиться с помощью такого значения аргумента end:

```py
def value(items):
    for item in items:
        print(item, end=' ')


value([1,2,3,4])
# 1 2 3 4
```

## Переменные

Переменные содержат данные. Благодаря этому к ним можно обращаться, заново использовать, вызывать, назначать и так далее.
Понимать переменные важно для работы с любой логикой в программировании. Это то, что знает любой программист вне зависимости от языка программирования, и поэтому это так важно для начинающих.
Простейшее определение переменной — это именованный контейнер для данных, к которым нужно обращаться в программе. Есть 2 основные причины для этого:

- Зачастую данные — это больше чем 2 символа.
- Обычно к ним нужно обращаться по несколько раз.

### Где используется?

- Сложно представить программирование без переменных. Это как обращаться к людям, не используя их имена и фамилии. Можно только представить, насколько это было бы неудобно.
- В программировании переменные используются для определения и обращения к данным разных размеров, типов и форм.

### Правила использования

- При присвоении значения переменная всегда находится слева, а данные — справа.
- Имя переменной может начинаться с символа или нижнего подчеркивания (`_`), но не с числа.
- Для вывода значения переменной с помощью функции print нужно передавать ее без кавычек.
- Переменные создаются по принципу: `<имя> = <значение>`.
- Не смотря на поддержку русских названий переменных, рекомендуется использовать латинские названия.
- Есть негласные правила для названий. Для переменных, объектов, функций, иногда констант это snake_case (маленькми буквами, слова отделяются нижним подчеркиванием), а для классов - CamelCase (большими буквами, первая буква большая). Для констант применяется так же UPPER_CASE (большими буквами, через нижнее подчеркивание).
- Так же рекомендуется избегать транслита. Лучше назвать переменную variable, а не peremennaya.

### Частые ошибки

- Начинать имя переменной с цифры.
- Использовать символы (кроме нижнего подчеркивания) в имени переменной.
- Использовать в переменной пробелы.

### Примеры использования переменных

Предположим, что есть большое число: `149597970`. Оно обозначает расстояние между Солнцем и Землей в километрах.
Предположим, что к этому значению нужно обратиться для выполнения вычислений. Вместо того, чтобы каждый раз вводить его, можно просто использовать переменную. Вот так:

```py
>>> sun_to_earth = 149597970
>>> sun_to_earth = sun_to_earth + 1
>>> print(sun_to_earth)
149597971
```

**Разберем код примера:**
Сначала создается переменная `sun_to_earth`, и ей присваивается значение `149597970`.
Переменной `sun_to_earth` присваивается новое значение — `149597971`.

Переменные - это место в памяти, куда можно сохранить данные.

```py
a = 1 + 2 # 3
b = "123"
c = True
d = None
print(a, b, c, d) # 1 123 True None
```

Парочка интересных моментов языка

1. При выводе на экран значение переменной никуда не девается и мы можем вывести значение сколько раз угодно
2. print все еще может выводить значения одновременно с переменным
3. В отличии от многих других языков в python отсутствует типизация и ему абсолютно параллельно, что мы будем присваивать переменной - новое число или новую строку. Делать мы можем это сколько раз угодно. При новом присваивании питон автоматически меняет тип переменной
4. Мы можем указывать эту переменную в вычислениях, про операции с переменными и константами мы поговорим отдельно
5. Мы можем резко поменять то, что хранится в переменной - было число, стало строка

## Ввод

```py
name = input("Введите ваше имя: ") # Вводим имя
print("Привет, ", name) # Выводим приветствие
```

input - это функция, которая требует 1 аргумент, это строка, которая будет выведена перед вводом. Возвращает введенную строку.
print - к слову, тоже функция, но на вход принимает любое количество аргументов, которые будут распечатаны. Возвращает None.

## Типы данных

Основных типо данных несколько. Сейчас говорится не о всех

| Тип     | Описание                 | Пример               |
| ------- | ------------------------ | -------------------- |
| int     | Целое число              | 123                  |
| float   | Число с плавающей точкой | 1.23                 |
| str     | Строка                   | "Hello, world!"      |
| bool    | Логическое значение      | True, False          |
| complex | Комплексное число        | 1 + 2j               |
| none    | Значение не определено   | None                 |
| list    | Список                   | \[1, 2, 3\]          |
| set     | Множество                | {1, 2, 3}            |
| tuple   | Кортеж                   | (1, 2, 3)            |
| dict    | Словарь                  | {1: "one", 2: "two"} |

### Строки

#### Про кавычки

`"1"` и `'1'` - эти 2 записи - одно и тоже
`"строка в "кавычках""` - такая запись вызовет ошибки, изза того, что питон запутается в одинаковых кавычках
`'тут "кавычки"'` - тут питон не запутался в кавычках, так как они разные
`"тут 'кавычки'"` - кавычки можно комбинировать, все четыре типа кавычек (`'`, `"`, `"""`, `'''`) можно комбинировать, главное, что бы строка начиналась и заканчивалась одним типом кавычек
`'текст \'в\' кавычках'` - тут с помощью `\` кавычки были _экранизированы_, и теперь питон не запутается
`" 123 \" 123"` - тот же самый случай с другими кавычками

#### Про `\`

`\` внутри строки отвечает за вывод некоторых символов и экранизацию, пока что просто помните, что:
`\" \'` - "защищеные" от поломки кода кавычки, которые можно использовать в тексте
`\\` - вывод `\` без каких либо экранизаций и прочего
`\n \t` - новая строка и табуляция (как при нажатии на Tab)

#### Про мультистроки

Иногда бывает очень много текста, который содержит переносы строк (`\n`), тогда можно использовать мультистроки, который можно растягивать на любое количество строк кода, в то время как обычные - нельзя:

```py
print("""
Этот текст содержит множество
переносов
строк
и огромное количество текста...
""")
# Убрать первый перенос строки
print("""\
123
123
""")
```

1. `'''` и `"""` - опять же одно и тоже
2. Экранизировать `'` внутри `'''` или `"` внутри `"""` - не надо, питон запутается лишь если вы напечатаете сразу 3 кавычки подряд внутри мультстроки
3. Если вы сразу после первой тройной кавычки ставите перенос строки - то при выводе на экран у вас выведется одна пустая строка. Что бы этого избежать - поставьте `\` который уберет эту лишнюю пустую строку. Так же можно писать любой текст сразу после тройных кавычек вместо `\`

### Целые числа (int), комплексные (complex) и вещественные числа (float)

#### Целые числа (int)

Числа в Python 3 ничем не отличаются от обычных чисел. Они поддерживают набор самых обычных математических операций:

| Операция         | Описание                         |
| ---------------- | -------------------------------- |
| x + y            | Сложение                         |
| x - y            | Вычитание                        |
| x \* y           | Умножение                        |
| x / y            | Деление                          |
| x // y           | Получение целой части от деления |
| x % y            | Остаток от деления               |
| \-x              | Смена знака числа                |
| abs(x)           | Модуль числа                     |
| divmod(x, y)     | Пара (x // y, x % y)             |
| x \*\* y         | Возведение в степень             |
| pow(x, y\[, z\]) | xy по модулю (если модуль задан) |

#### Длинная арфиметика

Также нужно отметить, что целые числа в python 3, в отличие от многих других языков, поддерживают длинную арифметику (однако, это требует больше памяти).

```py
>>> 255 + 34
289
>>> 5 * 2
10
>>> 20 / 3
6.666666666666667
>>> 20 // 3
6
>>> 20 % 3
2
>>> 3 ** 4
81
>>> pow(3, 4)
81
>>> pow(3, 4, 27)
0
>>> 3 ** 150
369988485035126972924700782451696644186473100389722973815184405301748249
```

#### Побитовые операции

Над целыми числами также можно производить битовые операции

| Операция | Описание                    |
| -------- | --------------------------- |
| x \| y   | Побитовое _или_             |
| x ^ y    | Побитовое _исключающее или_ |
| x & y    | Побитовое _и_               |
| x << n   | Битовый сдвиг влево         |
| x >> y   | Битовый сдвиг вправо        |
| ~x       | Инверсия битов              |

#### Дополнительные методы

int.bit_length() - количество бит, необходимых для представления числа в двоичном виде, без учёта знака и лидирующих нулей.

```py
>>>
>>> n = -37
>>> bin(n)
'-0b100101'
>>> n.bit_length()
6
```

int.to_bytes(length, byteorder, \*, signed=False) - возвращает строку байтов, представляющих это число.

```py
>>>
>>> (1024).to_bytes(2, byteorder='big')
b'\x04\x00'
>>> (1024).to_bytes(10, byteorder='big')
b'\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00'
>>> (-1024).to_bytes(10, byteorder='big', signed=True)
b'\xff\xff\xff\xff\xff\xff\xff\xff\xfc\x00'
>>> x = 1000
>>> x.to_bytes((x.bit_length() // 8) + 1, byteorder='little')
b'\xe8\x03'
classmethod int.from_bytes(bytes, byteorder, *, signed=False) - возвращает число из данной строки байтов.
```

```py
>>>
>>> int.from_bytes(b'\x00\x10', byteorder='big')
16
>>> int.from_bytes(b'\x00\x10', byteorder='little')
4096
>>> int.from_bytes(b'\xfc\x00', byteorder='big', signed=True)
-1024
>>> int.from_bytes(b'\xfc\x00', byteorder='big', signed=False)
64512
>>> int.from_bytes([255, 0, 0], byteorder='big')
16711680
```

#### Системы счисления

Те, у кого в школе была информатика, знают, что числа могут быть представлены не только в десятичной системе счисления. К примеру, в компьютере используется двоичный код, и, к примеру, число 19 в двоичной системе счисления будет выглядеть как 10011. Также иногда нужно переводить числа из одной системы счисления в другую. Python для этого предоставляет несколько функций:

- `int([object], [основание системы счисления])` - преобразование к целому числу в десятичной системе счисления. По умолчанию система счисления десятичная, но можно задать любое основание от 2 до 36 включительно.
- `bin(x)` - преобразование целого числа в двоичную строку.
- `hex(х)` - преобразование целого числа в шестнадцатеричную строку.
- `oct(х)` - преобразование целого числа в восьмеричную строку.

```py
>>> a = int('19') # Переводим строку в число
>>> b = int('19.5')  # Строка не является целым числом
Traceback (most recent call last):
  File "", line 1, in
ValueError: invalid literal for int() with base 10: '19.5'
>>> c = int(19.5)  # Применённая к числу с плавающей точкой, отсекает дробную часть
>>> print(a, c)
19 19
>>> bin(19)
'0b10011'
>>> oct(19)
'0o23'
>>> hex(19)
'0x13'
>>> 0b10011  # Так тоже можно записывать числовые константы
19
>>> int('10011', 2)
19
>>> int('0b10011', 2)
19
```

#### Вещественные числа (float)

Вещественные числа поддерживают те же операции, что и целые. Однако (из-за представления чисел в компьютере) вещественные числа неточны, и это может привести к ошибкам:

```py
>>>
>>> 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1
0.9999999999999999

```

Для высокой точности используют другие объекты (например Decimal и Fraction)).

Также вещественные числа не поддерживают длинную арифметику:

```py
>>>
>>> a = 3 ** 1000
>>> a + 0.1
Traceback (most recent call last):
  File "", line 1, in
OverflowError: int too large to convert to float
```

Простенькие примеры работы с числами:

```py
>>>
>>> c = 150
>>> d = 12.9
>>> c + d
162.9
>>> p = abs(d - c)  # Модуль числа
>>> print(p)
137.1
>>> round(p)  # Округление
137
```

Дополнительные методы

- `float.as_integer_ratio()` - пара целых чисел, чьё отношение равно этому числу.

- `float.is_integer()` - является ли значение целым числом.

- `float.hex()` - переводит float в hex (шестнадцатеричную систему счисления).

- `classmethod float.fromhex(s)` - float из шестнадцатеричной строки.

```py
>>>
>>> (10.5).hex()
'0x1.5000000000000p+3'
>>> float.fromhex('0x1.5000000000000p+3')
10.5
```

Помимо стандартных выражений для работы с числами (а в Python их не так уж и много), в составе Python есть несколько полезных модулей.

Модуль math предоставляет более сложные математические функции.

```py
>>>
>>> import math
>>> math.pi
3.141592653589793
>>> math.sqrt(85)
9.219544457292887
```

Модуль random реализует генератор случайных чисел и функции случайного выбора.

```py
>>>
>>> import random
>>> random.random()
0.15651968855132303
```

#### Комплексные числа (complex)

В Python встроены также и комплексные числа:

```py
>>> x = complex(1, 2)
>>> print(x)
(1+2j)
>>> y = complex(3, 4)
>>> print(y)
(3+4j)
>>> z = x + y
>>> print(x)
(1+2j)
>>> print(z)
(4+6j)
>>> z = x * y
>>> print(z)
(-5+10j)
>>> z = x / y
>>> print(z)
(0.44+0.08j)
>>> print(x.conjugate())  # Сопряжённое число
(1-2j)
>>> print(x.imag)  # Мнимая часть
2.0
>>> print(x.real)  # Действительная часть
1.0
>>> print(x > y)  # Комплексные числа нельзя сравнить
Traceback (most recent call last):
  File "", line 1, in
TypeError: unorderable types: complex() > complex()
>>> print(x == y)  # Но можно проверить на равенство
False
>>> abs(3 + 4j)  # Модуль комплексного числа
5.0
>>> pow(3 + 4j, 2)  # Возведение в степень
(-7+24j)
```

Для работы с комплексными числами используется также модуль cmath.

## Завершение

Статья может быть моментами неточной. Я буду рад почитать ваши комментари :)

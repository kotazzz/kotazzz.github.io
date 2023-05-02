import os

# путь до папки content
path = './content/post'

# создаем новый файл text.txt и открываем его для записи
with open('text.txt', 'w') as f:
  # проходим по всем файлам и папкам внутри папки content
  for item in os.listdir(path):
    # проверяем, является ли текущий элемент папкой и содержит ли папка файл index.md
    if os.path.isdir(os.path.join(path, item)) and 'index.md' in os.listdir(os.path.join(path, item)):
      # открываем файл index.md и читаем первые 10 строк
      with open(os.path.join(path, item, 'index.md')) as f_index:
        head = [next(f_index) for x in range(10)]
      # записываем название папки и первые 10 строк в новый файл text.txt
      f.write(f'{item}\n')
      f.writelines(head)
      f.write('\n')

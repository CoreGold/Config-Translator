# Преобразователь текста из формата TOML в пользовательский конфигурационный формат

Этот проект представляет собой преобразователь файлов TOML в пользовательский конфигурационный формат. Он позволяет загружать данные из TOML файла, преобразовывать их в специальный формат и сохранять результат в новый файл.
Значения:
• Числа.
• Словари.
• Константные вычисления.

## Установка

Для работы с проектом потребуется Python 3 и библиотека tomlkit.

## Использование

### Запуск из командной строки

Вы можете использовать скрипт из командной строки следующим образом:

python Translator.py <inputfile.toml> <output_file.txt>

- <input_file.toml>: Путь к входному файлу в формате TOML.
- <output_file.txt>: Путь к выходному файлу, где будет сохранён преобразованный результат.

### Тестирование

Предположим, у вас есть файл config.toml со следующим содержимым:

```
#Hello
#Hello2

title = 1

title2 = '?{title + 5}'
[[emloyees]]
id = 213
name = "franc"
  [[emloyees.others]]
  department = "sales"
  did = 1
    [[emloyees.others.test]]
    k = '?{did max 99}'
    [[emloyees.others.test]]
    kk = 3
  [[emloyees.others]]
  salary = 5_000

title3 = "test"

[server]
host = "localhost"
port = 8080
ssl = 1
```

Вы можете запустить преобразование следующей командой: 

python Translator.py config.toml output.txt

После выполнения команды файл output.txt будет содержать:
Комментарии.
```
//Hello

//Hello2
```
Константные выражения и вычисления.
```
title = 1

title2 = 6
```
Словари, в том числе вложенные.
```
$[
  id: 213 
  $[
    did: 1 
    $[
    k: 99 
    ]
    $[
    kk: 3 
    ]
  ]
  $[
    salary: 5000 
  ]
]

$[
  port: 8080 
  ssl: 1 
]
```
Все значение кроме чисел, словарей и константных вычислений игнорируются.


Кроме этого, готовые тесты программы с использованием unittest предложены в файле Test_Translator.py





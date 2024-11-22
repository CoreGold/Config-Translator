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
title3 = "test"

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
Все значения кроме чисел, словарей и константных вычислений игнорируются.


Кроме этого, готовые тесты-программы и готовые тестовые файлы предложены в Test_Translator.py

# Примеры работы преобразователя
### 1. Пользователи сети

Toml
```
[users]

[[users.admin]]
id = 1
max_permissions_level = 10
session_timeout_minutes = 30

[[users.guest]]
id = 2
max_permissions_level = 1
session_timeout_minutes = 5

[[users.moderator]]
id = 3
max_permissions_level = 5
session_timeout_minutes = 15
```

Учебный конфигурационный язык
```
$[
  $[
    id: 1 
    max_permissions_level: 10 
    session_timeout_minutes: 30 
  ]
  $[
    id: 2 
    max_permissions_level: 1 
    session_timeout_minutes: 5 
  ]
  $[
    id: 3 
    max_permissions_level: 5 
    session_timeout_minutes: 15 
  ]
]
```

### 2. Настройки компьютерной игры 

Toml
```
#Game Settings

[graphics]
resolution_width = 1920
resolution_height = 1080
fullscreen_mode = 1
vsync_enabled = 0
anti_aliasing_level = 4

[audio]
volume_master = 80
volume_music = 50
volume_effects = 70
mute_audio = 0
```

Учебный конфигурационный язык
```
//Game Settings

$[
  resolution_width: 1920 
  resolution_height: 1080 
  fullscreen_mode: 1 
  vsync_enabled: 0 
  anti_aliasing_level: 4 
]

$[
  volume_master: 80 
  volume_music: 50 
  volume_effects: 70 
  mute_audio: 0 
]
```
### 3. Настройки сервера

Toml
```
[server]
ip_part1 = 127
ip_part2 = 0
ip_part3 = 0
ip_part4 = 1
port = 8080
https_enabled = 1  

[logging]
log_level = 2  
log_to_file = 1  

[database]
db_type_id = 1  
db_host_ip_part1 = 192
db_host_ip_part2 = 168
db_host_ip_part3 = 1
db_host_ip_part4 = 10
db_port = 5432
```

Учебный конфигурационный язык
```
$[
  ip_part1: 127 
  ip_part2: 0 
  ip_part3: 0 
  ip_part4: 1 
  port: 8080 
  https_enabled: 1 
]

$[
  log_level: 2 
  log_to_file: 1 
]

$[
  db_type_id: 1 
  db_host_ip_part1: 192 
  db_host_ip_part2: 168 
  db_host_ip_part3: 1 
  db_host_ip_part4: 10 
  db_port: 5432 
]
```

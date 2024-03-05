### Описание проекта.
Реализован сервис с следующим функционалом с на языке Python 
использованием фреймворка Django.
1. В базе данных Postgres имеется таблица currency c колонками:
    - id — первичный ключ
    - name — название валюты
    - rate — курс валюты к рублю

2. Консольная команда «python manage.py import data» обновляет данные в таблице currency. Данные
по курсам валют берутся отсюда: http://www.cbr.ru/scripts/XML_daily.asp

3. Реализовано 2 REST API(JSON RPC 2.0) метода:
    - GET /currencies — возвращает список курсов валют
        -- возможность пагинации
    - GET /currency/ — возвращает курс валюты для переданного id

4. Добавлена аутентификация по JWT-токену.

5. Добавлены тесты:
    - при указании в заголовке токена пользователь имеет доступ к currencies
    - при указании в заголовке токена пользователь имеет доступ к currency
    - без указания в заголовке токена пользователь не имеет доступ к currencies
    - без указания в заголовке токена пользователь не имеет доступ к currency

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Practic73/rk_project
```

```
cd api_yamdb
```

Cоздать и активировать виртуальное окружение:

Windows
```
python -m venv venv
source venv/Scripts/activate
```
Linux/macOS
```
python3 -m venv venv
source venv/bin/activate
```

Обновить PIP

Windows
```
python -m pip install --upgrade pip
```
Linux/macOS
```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

Windows
```
python manage.py makemigrations
python manage.py migrate
```

Linux/macOS
```
python3 manage.py makemigrations
python3 manage.py migrate
```

Заполнить базу данных:

Windows
```
python manage.py insert data
```

Linux/macOS
```
python3 manage.py insert data
```

Запустить проект:

Windows
```
python manage.py runserver
```

Linux/macOS
```
python3 manage.py runserver
```
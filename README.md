## Технологий

- Python 3.9
- Django 3.2
- DRF

Cоздать и активировать виртуальное окружение:
```
python3 -m venv venv
```
```
source venv/bin/activate
```
Установить PostgreSQL
```
brew install postgresql
```
Восстанавливаем базу данных из дампа
```
psql review < review.bak
```
Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```

Выполнить миграции:
```
python manage.py migrate
```
Запустить проект:
```
python3 manage.py runserver
```

## Примеры работы с API для всех пользователе

```
GET api/country/ - получить список стран.
GET api/country/{id}/ - получение страны по id
GET api/manufacturer/ - получение списка доступных производств
GET api/manufacturer/{id}/ - получение информации о производстве по id
GET api/cars/ - получение списка автомобилей
GET api/cars/{id}/ - Получение автомобиля по id
GET api/comment/{id}/ - Получение комментариев
GET api/comment/{id}/ - Получение комментариев по id

```

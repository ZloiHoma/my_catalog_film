# Каталог фильмов — Django проект

Проект реализует сайт-каталог домашней коллекции фильмов с тремя страницами:
- Главная: список фильмов с постерами, названиями и годами
- Детали фильма: описание, режиссёр, актёры
- Топ-5: пронумерованный список любимых фильмов

## Установка

```bash
# Создать виртуальное окружение
python -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate     # Windows

# Установить зависимости
pip install -r requirements.txt

# Запустить миграции
python manage.py makemigrations
python manage.py migrate

# Создать суперпользователя (для админки)
python manage.py createsuperuser

# Запустить сервер
python manage.py runserver
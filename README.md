# Estetis - Тествое задание
Этот репозиторий содержит реализацию тестового задания Estetis. Проект представляет собой REST API микросервис, написанный на языке Python с использованием фреймворка FastAPI. Он предоставляет функциональность для добавления, получения и обновления задач.
<hr>

### Запуск на локальном компьютере
    
    # Клонируйте репозиторий
    git clone https://github.com/byplentik/Estetis.git

    # Создайте папку с зависимостями
    py -m venv venv
    cd venv/scripts/activate
    pip install -r requirements.txt

    
    # Скачайте docker images и запустите контейнеры
    docker-compuse up -d --build

    # Примените миграции базы данных:
    docker exec -it estetis-app-1 alembic upgrade head

После выполнения этих шагов проект будет доступен по адресу http://localhost:8000.
<hr>

### Функциональность
- `POST` `/tasks/add/` Добавляет задачу в базу данных.
- `GET` `/tasks/` Получает все существующие задачи из базы данных.
- `PUT` `tasks/{uuid}` Обновляет задачу с заданным идентификатором (UUID).
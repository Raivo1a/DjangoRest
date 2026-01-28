# Платформа с онлайн курсами

## Описание
Платформа для онлайн-обучения

## Тестирование
Протестированы CRUD для классов Course и Lesson, а также управления подпиской

## В состав проекта входят:
1. PostgreSQL — база данных
2. Redis — брокер сообщений для Celery
3. Celery Worker — для выполнения фоновых задач
4. Celery Beat — для планирования периодических задач

### Запуск проекта

1. Установите Docker и Docker Compose, если они ещё не установлены
2. В терминале, перейдите в директорию проекта
3. Запустите команду:
docker-compose up

## Установка

### Локально

* Клонируйте репозиторий:
git clone https://github.com/Raivo1a/DjangoRest

* Установите зависимости
poetry install

* Активируйте виртуальное окружение
poetry shell

* Заполните переменные
cp .env.sample .env

* Примените миграции к базе данных
python manage.py migrate

* Запустите проект
python manage.py runserver

Веб-приложение будет доступно по адресу: http://localhost:8000

### Сервер

158.160.195.221

### Настройка сервера (через терминал)

* Запустите сервер:
ssh SSH_USER@IP_SERVER

* Обновите системы:
sudo apt update
sudo apt upgrade

* Установите Docker compose:
https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository

* Активируйте файрвол:
status ufw enable

* Откройте порты:
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw allow 22/tcp

### CI/CD

* Автоматически при push, pull_request:
Собирает Docker-образ
Пушит в Docker Hub
Разворачивает на сервере через SSH

## Команды:

Для просмотра запущенных контейнеров:
docker-compose ps

Для просмотра логов всех контейнеров:
docker-compose logs

Для остановки сервисов и удаления контейнеров:
docker-compose down

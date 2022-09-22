
IP: 178.154.192.231

### Описание:

Тестовое задание для OOO "Ришат". Создана API с простейшей HTML страницей для покупок онлайн по стредствам платежной системы Stripe.


###### Доступные адресса запросов:

1. .../admin/
2. .../item/{id}
3. .../buy/{id}


### Установка:

Для начала вам необходимо сделать Fork данного проекта к себе в профиль.

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/<ваш_ник>/<Имя_проекта>.git
```

Перейти в папку **infra**, создать файл **.env**, внести в него необходимые переменные.

```
DB_ENGIINE= # Основа базы данных
DB_NAME= # Имя базы данных
POSTGRES_USER= # Супер прользователь для взаимодействия с базой
POSTGRES_PASSWORD= # Пароль для пользователя
DB_HOST= # Хост внутри контейнера для базы данных
DB_PORT= # Порт внутри контейра
SECRET_KEY= #Секретны ключ джанго
STRIPE_SECRET_KEY= #Секретны ключ Stripe
STRIPE_PUBLIC_KEY= #Публичный ключ Stripe
```

Перейти в папку с файлом `Docker` и выполнить команды:

```commandline
docker build -t <ник Docker_hub>/<имя_проекта>:v0.9 .
docker push <ник Docker_hub>/<имя_проекта>:v0.9
```

Внесите изменения в файле /infra/docker-compose.yaml

```
web:
  image: <ник Docker_hub>/<имя_проекта>:v0.9
```

Подключиться на удаленный сервер, скопировать файлы из папки `infra` (.env, docker-compose.yaml, директорию nginx c файлом dafault.conf)

Запустить развертывание:
```commandline
sudo docker-compose up -d --build
```

После получения сообщения об успешном развертывании, подключиться на удаленный сервер и выполнить миграции:

```
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input 
```

Наполнить базу данными по средствам ***The Django admin site***

# stripe-test-assignment

Django Backend with Stripe API payments attached

Предполагается, что у вас на машине установлен docker-compose

Для запуска требуется:

1. Склонировать репозиторий к себе  
   `git clone https://github.com/FrankRowlinson/stripe-test-assignment.git`

2. Создать .env файл со следующими переменными окружения:  
   `SECRET_KEY` - секретный ключ самого django, можно сгенерировать с помощью встроенной в Django утилиты `django.core.management.utils.get_random_secret_key`  
   `STRIPE_PUBLIC_API_KEY` - публичный ключ API Stripe, можно получить в личном кабинете Stripe после создания аккаунта  
   `STRIPE_SECRET_API_KEY` - секретный ключ API Stripe, см. выше  
   `ALLOWED_HOSTS=localhost,127.0.0.1`
   `DEBUG=True` - отладка, удобнее менять через переменные окружения

3. Создать и запустить контейнер с помощью команды:  
   `docker compose --rm -p 8000:8000 app`

4. Тестировать на `localhost:8000` или `127.0.0.1:8000`

P.S. Для тестов доступны два объекта Item, с ключами 1 и 2. Для доступа к ним можно обращаться по  
`localhost:8000/item/1/`, тогда будет страничка покупки и перенаправление на Stripe, или через  
`localhost:8000/buy/1/`, тогда API вернет json-файл с айди сессии **Stripe Session**.

# Автоматизированный сбор информации о сети

Перед нами стояла задача реализовать механизм сбора информации о сети в Linux и представить полученные данные в веб-интерфейсе.

С помощью нашего веб-сервиса вы можете:
  - Отслеживать состояния открытых соединений в данный момент(Протокол, локальный адрес, внешний адрес)
  - Иметь доступ к информации о текущей настройке сети (IP адресация, маска, бродкаст и интерфейс, который используется для выхода в глобальную сеть)
  - Отслеживать пакеты, которые проходят через аппаратный интерфейс

### Как использовать веб-интерфейс? 

Для запуска API необходимо наличие python. Предпочтительная версия python - 3.6
```sh
$ python3.6 ./manage.py runserver
```

Для запуска веб-интерфейса мы используем npm v5.6.0 node v9.11.2.

```sh
$ npm start
```

### Перспективы

Текущую систему возможно расширить до создания полноценного веб-приложения для сбора статистики об использовании сети конкретным пользователем. 
В перспективе будет происходить сканирование не определённой сети, в которой запущен сервер, а создание  пакетов с нашим функционалом для пользователей. Это позволит собирать информацию с их компьютеров и централизованно хранить на нашем сервере. Такой вариант был бы актуален для корпораций, чтобы вести контроль и следить за безопасностью сети.

# PWS-15_d6_petshouse

## Доступен в Heroku по адресу:
https://sheltered-lowlands-17515.herokuapp.com

## Установка и запуск локально (все действия через коммандную строку)
  - скачать проект и перейти в директорию проекта
  ```
$ git clone https://github.com/LovingFox/PWS-15_d6_petshouse
$ cd PWS-15_d6_petshouse
```
  - создать виртуальное окружение
  ```
$ python -m venv env
```
  - применить виртуальное окружение
```
### Если у вас Linux:
$ source env/bin/activate
### Если у вас Windows:
$ env\Scripts\activate.bat
```
 - установить зависимости
  ```
$ pip install -r requirements.txt
```

  - запустить сервер
  ```
$ python manage.py runserver
```

## Использование локально
- открыть страницу http://127.0.0.1:8000/
- админка http://127.0.0.1:8000/admin (username: admin, password: pass)


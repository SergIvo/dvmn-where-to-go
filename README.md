# Куда пойти

Сайт проекта "Куда пойти" - интерактивной карты с указанными на ней интересными местами для посещения. Ссылка на демо-версию сайта: [sergivo.pythonanywhere.com/](https://sergivo.pythonanywhere.com/)

## Установка и запуск

- Скачайте код командой `git clone`:
```command line
git clone https://github.com/SergIvo/dvmn-where-to-go
```
- Создайте и запустите виртуальное окружение:
```command line
python -m venv venv
source venv/bin/activate
```
- Установите необходимые библиотеки из файла `requirements.txt`:
```command line
pip install -r requirements.txt
```
Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны следущие переменные:
- `DEBUG` — дебаг-режим. Поставьте `True`, чтобы увидеть отладочную информацию в случае ошибки. Выключается значением `False`.
- `SECRET_KEY` — секретный ключ проекта. Например: `erofheronoirenfoernfx49389f43xf3984xf9384`.
- `ALLOWED_HOSTS` — см [документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts).
- `STATIC_URL` — по-умолчанию это `'/static/'`. [Что такое STATIC_URL](https://docs.djangoproject.com/en/3.0/ref/settings/#std:setting-STATIC_URL).
- `STATIC_ROOT` — по-умолчанию это `'None'`, т.е. текущая папка. [Что такое STATIC_ROOT](https://docs.djangoproject.com/en/3.0/ref/settings/#std:setting-STATIC_ROOT).
- `MEDIA_URL` — по-умолчанию это `'/media/'`. [Что такое MEDIA_URL](https://docs.djangoproject.com/en/3.0/ref/settings/#std:setting-MEDIA_URL).
- `MEDIA_ROOT` — по-умолчанию это `'media'`. [Что такое MEDIA_ROOT](https://docs.djangoproject.com/en/3.0/ref/settings/#std:setting-MEDIA_ROOT).

**Чтобы запустить проект локально, эти настройки не требуются**, значения уже проставлены по-умолчанию. Однако для запуска проекта на реальном сервере часть значений необходимо заменить, а именно
`DEBUG`, `SECRET_KEY` и `ALLOWED_HOSTS`. Подробнее об этом можно [почитать здесь](https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/).

- Запустите сервер следующей командой: 
```command line
python3 manage.py runserver
```

После этого переходите по ссылке [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Цели проекта

Код написан в учебных целях в рамках курса по веб-разработке на сайте [Devman](https://dvmn.org).

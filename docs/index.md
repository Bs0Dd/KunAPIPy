<h1 align="center">  KunAPIPy </h1>
<h1 align="center">  api.kundelik.kz wrapper </h1>
<p align="center">Упрощение работы с API Казахстанского электронного дневника как с токеном, так и без него.</p>
<p align="center">Основан на Враппере DnevnikRuAPI.</p>

## Установка

```sh
pip install https://github.com/Bs0Dd/KunAPIPy/archive/master.zip --upgrade
```

## Пример синхронного использования

#### Получение домашнего задания на указанный период без токена.

```python3
from kunapipy.kundelik import kundelik
from datetime import datetime

login = "login"
password = "password"
# Получаем доступ через логин и пароль

dn = kundelik.KunAPI(login=login, password=password)

print(
    dn.get_school_homework(1000002283077, datetime(2019, 9, 5), datetime(2019, 9, 15))
)
#  Получение домашнего задания текущего пользователя для школы с id 1000002283077 в период с 05-09-2019 по 15-09-2019

print(dn.get_edu_groups())
#  Получение групп обучения текущего пользователя
```

## Пример асинхронного использования

#### Получение домашнего задания на указанный период без токена.

```python3
from kunapipy.asynkundelik import kundelik
from kunapipy.asynkundelik.utils import TaskManager
import asyncio
from datetime import datetime


async def get_dn_info():
    homework = await dn.get_school_homework(
        1000002283077, str(datetime(2019, 9, 5)), str(datetime(2019, 9, 15))
    )
    #  Получение домашнего задания текущего пользователя для школы с id 1000002283077 в период с 05-09-2019 по 15-09-2019
    print(homework)

    edu_groups = await dn.get_edu_groups()
    #  Получение групп обучения текущего пользователя
    print(edu_groups)


async def close_session():
    await dn.close_session()
    #  В конце использования закрываем сессию


if __name__ == "__main__":
    login = "login"
    password = "password"
    dn = kundelik.AsyncKunAPI(login=login, password=password)
    # Получаем доступ через логин и пароль

    loop = asyncio.get_event_loop()
    # Добавляем все наши функции в event loop через Task Manager

    task_manager = TaskManager(loop)
    task_manager.add_task(get_dn_info)
    task_manager.run(on_shutdown=close_session)
    # Закрываем сессию по завершению работы

```

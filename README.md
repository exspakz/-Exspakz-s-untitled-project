# [Factory Bot]()


## Содержание

[1. Описание проекта](README.md#Описание-проекта)  
[2. Функционал](README.md#Функционал)  
[3. Установка и запуск](README.md#Установка-и-запуск)  


## Описание проекта

Простая реализация телеграм бота, как самостоятельно сервиса для API [Factory Backend](https://gitlab.com/exspa/factory-back) которое принимает сообщения и отправляет их в связанный с пользователем чат через бота.

:arrow_up: [к содержанию](README.md#Содержание)


## Функционал

#### Реализация и используемые технологии:

- Библиотека - pyTelegramBotAPI


:arrow_up: [к содержанию](README.md#Содержание)


## Установка и запуск

#### Клонируйте проект локально и перейдите в папку `bot`:

```bash
git clone https://gitlab.com/exspa/factory-telegram-bot.gi
```

#### Создайте виртуальное окружение для проекта:

```bash
python -m venv venv_factory_bot
source venv_factory_bot/bin/activate
```

#### Установите необходимые пакеты из файла `factory/requirements.txt`:
```bash
pip install -r factory/requirements.txt 
```

#### Создайте и зарегистрируйте Telegram bot по [инструкции](https://core.telegram.org/bots/features#botfather) для получения токена, после замените переменную окружения в файле `factory/.env.Example`:

```python
# bot
TOKEN='1234567890:SSKkiLSxo_2TheW4j3II8IDxKtCX_lLaTcN'
```

#### В файле `.env.Example` замените другие шаблонные переменные окружения если это необходимо:

```python
# factory api
DOMAIN='127.0.0.1:8000'
```

#### Запуск бота, выполните команду:

 - `python -m bot.handlers`

:arrow_up: [к содержанию](README.md#Содержание)
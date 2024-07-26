# GoodGames

GoodGames - это платформа, где пользователи могут ознакомиться с различными играми и получить подробную информацию о них.

## Особенности
1. Красивые и интуитивно понятные карточки игр
1. Возможность просматривать подробную информацию об играх
1. Адаптивный дизайн для комфортного использования на разных устройствах
1. Легкая навигация по сайту

## В разработке

1. Добавление рейтинга для каждой игры.
1. Возможность фильтровать карточки по рейтенгу.
1. Разделение карточек на разные страницы.
1. Изменение дизайна.
1. Добавление регистрации.
1. Поле для запроса на добавлению игры.
1. Добавление перевода на разные языки.


## Как установить



Python3 должен быть уже установлен. Затем используйте pip (или pip3, если есть конфликт с Python2) для установки зависимостей:

```
pip install -r requirements.txt
```


## Как запускать скрипты 

Для добавления игры нужно запустить `main.py`. Запустить файл можно через терминал:

```
python main.py
```

## Как использовать

Json файл `games.json` имеет такую структуру:
```
{
    "games": [
        {
            "name": "",
            "date": "",
            "author": "",
            "description": [],
            "requirements": {
                "min": [],
                "max": [],
                "technic": []
            },
            "img_url": "",
            "id": 0
        },
        ...
    ]
}
```
`name` - Название игры

`date` - Дата выхода

`author` - Создатель игры

`description` - Описание игры

`requirements` - Объект с характеристиками:

1. `min` - Минимальные требования к устройству
1. `max` - Рекомендованые требования к устройству
1. `technic` - На каких устройствах вышла игра

`img_url` - Картинка игры

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).


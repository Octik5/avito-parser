# avito-parser
Парсер Avito
## 🖨️ Document Template Generator
![Avito Parser](https://img.shields.io/badge/Python-3.8%2B-blue)
![Telegram API](https://img.shields.io/badge/Telegram%20API-Latest-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

![Avito Telegram Integration](https://i.pinimg.com/736x/c6/4d/f9/c64df982b36bc0ae4588a881ee7e1adb.jpg)

# Парсер новых объявлений Avito с уведомлением в Telegram

![Avito + Telegram]([https://example.com/avito-telegram-bot.jpg](https://i.pinimg.com/736x/c6/4d/f9/c64df982b36bc0ae4588a881ee7e1adb.jpg)) <!-- Замените на реальное изображение -->

Этот скрипт автоматически отслеживает новые объявления на Avito по заданным параметрам и отправляет уведомления в Telegram при появлении новых предложений.

## 🔥 Возможности

- Парсинг актуальных объявлений с Avito (с обходом защиты)
- Фильтрация уже отправленных объявлений
- Уведомления в Telegram-чат
- Поддержка случайных User-Agent для обхода блокировок
- Автосохранение истории отправленных объявлений

## ⚙️ Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/Octik5/avito-parser.git
cd avito-parser
```
# Установите зависимости:
```
pip install -r requirements.txt
```

Настройте параметры в коде:
```
TELEGRAM_BOT_TOKEN = 'ваш_токен_botfather'
TELEGRAM_CHAT_ID = 'ваш_chat_id'
```

## 🛠 Настройка
Получение Telegram данных
```
    Создайте бота через @BotFather

    Узнайте свой chat_id через @userinfobot
```
Настройка поиска
Замените URL в переменной url на ваш запрос с Avito:
```
url = "https://www.avito.ru/ваш_город/категория?параметры"
```
## 🚀 Запуск
```
python avito_parser.py
```

Скрипт будет проверять новые объявления каждые 5 минут.
## 📌 Важно!

    Avito может блокировать частые запросы - рекомендуемый интервал не менее 5 минут

    Для стабильной работы нужен качественный прокси (не включено в текущую версию)

    Сохраняйте sent_links.json между запусками для избежания дублирования

## 📄 Логирование
```bash
Все операции логируются в консоль:
🔍 Начинаем парсинг Avito...
Найдено 25 объявлений
🔹 Новое объявление: Корпус для ПК Deepcool
https://www.avito.ru/...
✅ Сообщение отправлено в Telegram
⏳ Ожидаем 5 секунд до следующей проверки...
```

## 📜 Лицензия

MIT License

## 💡 Совет: Для 24/7 работы разместите скрипт на VPS или Raspberry Pi

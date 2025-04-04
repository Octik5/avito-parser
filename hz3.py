import requests
from bs4 import BeautifulSoup
import time
import random
from fake_useragent import UserAgent
import json
import os

# 1. Настройки
TELEGRAM_BOT_TOKEN = '-'
TELEGRAM_CHAT_ID = '-'

# Инициализация UserAgent
ua = UserAgent()

# Загрузка отправленных ссылок
sent_links = set()
if os.path.exists('sent_links.json'):
    with open('sent_links.json', 'r') as f:
        sent_links = set(json.load(f))


def save_links():
    with open('sent_links.json', 'w') as f:
        json.dump(list(sent_links), f)


def get_headers():
    return {
        'User-Agent': ua.random,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        'Referer': 'https://www.avito.ru/',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }


def send_to_telegram(title, link):
    message = f"🔥 Новое объявление на Avito:\n\n{title}\n\n{link}"
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    try:
        response = requests.post(url, json={
            'chat_id': TELEGRAM_CHAT_ID,
            'text': message,
            'disable_web_page_preview': False
        })
        print("✅ Сообщение отправлено в Telegram" if response.status_code == 200 else f"⚠️ Ошибка: {response.text}")
    except Exception as e:
        print(f"⚠️ Ошибка Telegram: {e}")


def parse_avito(url):
    try:
        response = requests.get(url, headers=get_headers(), timeout=15)
        if response.status_code != 200:
            print(f"❌ Ошибка {response.status_code}")
            return None

        soup = BeautifulSoup(response.text, 'html.parser')

        # Новые селекторы для Avito 2024
        items = []
        for item in soup.select('[data-marker="item"], .iva-item-root'):
            try:
                link = item.find('a', href=True)
                if not link: continue

                full_url = f"https://www.avito.ru{link['href'].split('?')[0]}"
                title = item.find('h3', {'itemprop': 'name'}) or item.find('h3')
                title = title.get_text(strip=True) if title else "Без названия"

                items.append({
                    'title': title,
                    'url': full_url
                })
            except Exception as e:
                print(f"⚠️ Ошибка парсинга элемента: {e}")

        return items

    except Exception as e:
        print(f"⚠️ Ошибка запроса: {e}")
        return None


def main():
    url = "https://www.avito.ru/kazan/tovary_dlya_kompyutera/komplektuyuschie/korpus%D0%B0-ASgBAgICAkTGB~pm7gnEZw?cd=1&q=%D0%BA%D0%BE%D1%80%D0%BF%D1%83%D1%81+%D0%B4%D0%BB%D1%8F+%D0%BF%D0%BA+%D0%BA%D0%BE%D0%BC%D0%BF%D1%8C%D1%8E%D1%82%D0%B5%D1%80%D0%B0&s=104"
    last_ad_url = None  # Будем хранить URL последнего обработанного объявления

    while True:
        print("\n🔍 Начинаем парсинг Avito...")
        items = parse_avito(url)

        if items:
            print(f"Найдено {len(items)} объявлений")

            # Берем только первое объявление на странице
            first_item = items[0]

            # Проверяем, отличается ли оно от предыдущего
            if first_item['url'] != last_ad_url:
                print(f"\n🔹 Новое объявление:\n{first_item['title']}\n{first_item['url']}")

                # Проверяем, не отправляли ли мы его раньше
                if first_item['url'] not in sent_links:
                    send_to_telegram(first_item['title'], first_item['url'])
                    sent_links.add(first_item['url'])
                    save_links()
                    last_ad_url = first_item['url']  # Запоминаем как последнее обработанное
                else:
                    print("⏩ Это объявление уже было отправлено ранее")
            else:
                print("⏩ Первое объявление не изменилось")
        else:
            print("⚠️ Не удалось получить данные")


        delay = 300
        print(f"\n⏳ Ожидаем {delay // 60} минут до следующей проверки...")
        time.sleep(delay)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        save_links()
        print("\n🛑 Парсинг остановлен. Состояние сохранено.")
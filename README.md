# ☔ Rain Alert Bot (Telegram)

A Python-based weather notification system that checks the OpenWeatherMap API for upcoming rain in Aalsmeer and sends an automated alert via Telegram.

## 🚀 Features
* **Real-time Weather Check:** Analyzes the 3-hour forecast data.
* **Smart Notifications:** Only sends a message if the weather code indicates rain (codes < 700).
* **Automated Scheduling:** Powered by GitHub Actions to run every morning at 08:00 (NL time).
* **Secure:** Uses GitHub Secrets to keep API keys and tokens private.

## 🛠️ Tech Stack
* **Python 3.10**
* **Requests library** (for API calls)
* **GitHub Actions** (for automation)
* **Telegram Bot API**

## ⚙️ Setup & Installation

### 1. Prerequisites
* Get an API Key from [OpenWeatherMap](https://openweathermap.org/api).
* Create a Telegram Bot using [@BotFather](https://t.me/botfather) and get your `Bot Token`.
* Find your `Chat ID` using [@userinfobot](https://t.me/userinfobot).

### 2. Local Environment
Create a `secrets.py` file in the root directory (this file is ignored by Git):
```python
open_weather_key = "your_openweathermap_key"
telegram_token = "your_telegram_bot_token"
telegram_id = "your_telegram_chat_id"

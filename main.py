import requests
import os

try:
    from secrets import open_weather_key, telegram_token, telegram_id
except ImportError:
    open_weather_key = os.environ.get("OWM_API_KEY")
    telegram_token = os.environ.get("TELEGRAM_TOKEN")
    telegram_id = os.environ.get("CHAT_ID")


parameters = {

"appid": open_weather_key,
"units": "metric",
"lat" : 52.266750,
"lon" : 4.748940,
"cnt":4
}

weather_response = requests.get(url=f"https://api.openweathermap.org/data/2.5/forecast", params=parameters)
weather_response.raise_for_status()
data = weather_response.json()

will_rain = False
for item in data["list"]:
    condition_code = item['weather'][0]["id"]
    if condition_code < 700:
        will_rain = True
        break

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{telegram_token}/sendMessage"
    params = {
        "chat_id": telegram_id,
        "text": text
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    print("Success! Check your phone!.")

if will_rain:
    message = "☔ Thomas, it's going to rain in Aalsmeer! Bring your umbrella! "
    send_telegram_message(message)


import requests

from config import token_weather
from pprint import pp

TOKEN = token_weather

def get_weather(city: str):
    global TOKEN
    try:
        r = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={TOKEN}&units=metric")

        data = r.json()
        # pp(data)


        if r.status_code == 200:

            city_name = data["city"]["name"]
            country_name = data["city"]["country"]

            dict_day = {
                i_day["dt_txt"]: {
                    "Температура °C": i_day["main"]["temp"],
                    "Влажность %": i_day["main"]["humidity"],
                    "Давление гПа": i_day["main"]["pressure"],
                    "Ветер м/с": i_day["wind"]["speed"]
                }
                for i_day in data["list"][:3]
            }
            return city_name, country_name, dict_day
        else:
            return 401
    except Exception as ex:
        print(ex)

def main():
    city = "moscow"
    city_name, country_name, dict_day = get_weather(city=city)
    output = f"Город: {city_name}, Страна: {country_name}, \nПрогноз погоды:"
    print(output)
    pp(dict_day)


if __name__ == "__main__":
    main()

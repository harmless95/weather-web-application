import requests

from config import token_weather
from pprint import pp


def get_weather(city: str, token_wt):
    try:
        r = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={token_wt}&units=metric")
        data = r.json()
        pp(data)
        if data["cod"] == '200':
            print(200)
            city_name = data["city"]["name"]
            country_name = data["city"]["country"]

            list_day = [
                {"Дата": i_day["dt_txt"],
                 "Температура, °C": i_day["main"]["temp"],
                 "Влажность, %": i_day["main"]["humidity"],
                 "Давление, гПа": i_day["main"]["pressure"],
                 "Ветер, м/с": i_day["wind"]["speed"]}
                for i_day in data["list"][:3]
            ]
            output = f"Город: {city_name}, Страна: {country_name}, \nПрогноз погоды:"
            # for day in list_day:
            #     output += (f"\nДата: {day['Дата']}, "
            #                f"Температура: {day['Температура']}°C, "
            #                f"Влажность: {day['Влажность']}%, "
            #                f"Давление: {day['Давление']} гПа, "
            #                f"Ветер: {day['Ветер']} м/с")
            print(output)
            pp(list_day)
    except Exception as ex:
        print(ex)
        print("Проверьте название города")


def main():
    city = "moscow"
    get_weather(city=city, token_wt=token_weather)


if __name__ == "__main__":
    main()

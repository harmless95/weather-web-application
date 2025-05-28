from flask import Flask, abort
from main import get_weather

app = Flask(__name__)

@app.route("/weather_forecast/<string:city>", methods=["GET"])
def get_city_weather_forecast(city: str):
    if get_weather(city) == 404:
        return "Ошибка ввода", 404
    else:
        city_name, country_name, dict_w = get_weather(city)
        return f"Город: {city_name}\nСтрана: {country_name}\nПрогноз погоды:\n{dict_w}", 200

if __name__ == "__main__":
    app.run(debug=True)
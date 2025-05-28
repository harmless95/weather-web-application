from datetime import datetime
import unittest

from main import get_weather

class TestMain(unittest.TestCase):
    def setUp(self):
        self.city = "moscow"
        self.city_name, self.country_name, self.dict_day = get_weather(city=self.city)

    def test_out_city(self):
        "Проверяем город"
        city = "moscow"
        # проверяем город на тип и соответствие
        self.assertIsInstance(self.city_name, str)
        self.assertTrue(self.city_name.lower(), city)

    def test_out_country(self):
        "Проверяем данные страны"
        country = "RU"
        self.assertIsInstance(self.country_name, str)
        self.assertTrue(self.country_name, country)

    def test_out_dict_day(self):
        "Проверяем словарь прогноза погод по дням"
        temp = "Температура °C"
        humidity = "Влажность %"
        pressure = "Давление гПа"
        wind = "Ветер м/с"
        format_date = "%Y-%m-%d %H:%M:%S"
        # проверяем тип данных
        self.assertIsInstance(self.dict_day, dict)
        # проверяем требуемы данные в словаре для отображение информации
        for i_key, i_values in self.dict_day.items():
            with self.subTest(timestamp=i_key):
                self.assertIn(temp, i_values)
                self.assertIn(humidity, i_values)
                self.assertIn(pressure, i_values)
                self.assertIn(wind, i_values)
                # проверяем формат даты
                self.assertIsInstance(datetime.strptime(i_key, format_date), datetime)


    def test_error(self):
        "Проверяем вывод в случае ошибки"
        city_int = 234
        error = 401
        self.assertTrue(get_weather(city_int), error)

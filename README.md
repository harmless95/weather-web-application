# main.py
    ## файл содержит взаимодействие с API
        1. На сайте [Для перехода](https://home.openweathermap.org/api_keys) получаем или генерируем токен.
        2. Получаем URL [Для перехода](https://openweathermap.org/api/one-call-3) запрос указав вместо координат имя города.
        3. Получаем данные с помощью библиотеки requests.
        4. Меняем формат *.json(), из байтового в с ловарь json он может как серилизовать так и десерилизовать для передачи.
        5. Проверяем что данные пришли это указывает status_code если успешно 200, если не получилось 404
        6. Из словаря берем для работы:
            - Название города.
            - Название страны.
            - Прогноз погоды:
                + Температура, °C.
                + Влажность, %.
                + Давление, гПа.
                + Ветер, м/с.
        7. В словаре указан список прогноза погод по дате в виде словаря мы берем[:3] то есть первые 3.
        8. Весь блок мы проводили в try/except и в случае ошибки мы ее уловим и отобразим

# app.py
    ## Создаем приложение на Flask.
        1. Импортируем библеотеку from flask import Flask.
        2. Создаем экземпляр приложения app = Flask(__name__), где __name__ текущий модуль для использования пути.
        3. Указываем декоратор @app.route("/weather_forecast/<string:city>", methods=["GET"])
            - "/weather_forecast/<string:city>" URL запроса
                + <string:city> В строке запроса указываем город для получения информации.
            - methods=["GET"] в методе указываем тип запроса в данном случае это GET, но возможно POST, PATCH, DELETE.
        4. Создаем метод где будем получать город и отправлять в файл main.py где найдет и вернет нужные данные.
        5. Полученые данные передадим пользователь отправивший запрос.
        6. Запуск производится из текущего модуля if __name__ == "__main__":
        7. Приложение запускаем app.run() использовал debug=True для возможности изменения и тестирования в процессе.
# config.py
    ## В фале храним токкен для подключения API.
# test_main.py
    ## Делаем тесты где определяем файлы из API.
        1. Название файла должно начинаться на test_
        2. Импортируем библеотеку unittest
        3. В класс TestMain() берем из unittest TestCase.
        4. Создаем метод def setUp(self): И указываем там параметры, которые нам понадобятся во время всего процесса тестирования.
        5. Создаем методы где в каждом будут проводится определеные проверки, все методы должны начинаться на def test_.
            - def test_out_city(self):  метод для проверки города.
                + assert указаны:
                    ++ self.assertIsInstance(self.city_name, str) проверяем тип. 
                    ++ self.assertTrue(self.city_name.lower(), city) проверяем имя города из полученных данных.
            - def test_out_country(self): метод для проверки страны в котором находится город.
                + assert указаны:
                    ++ self.assertIsInstance(self.country_name, str) проверяем тип
                    ++ self.assertTrue(self.country_name, country) проверяем страну по названию города из полученных данных.
            - def test_out_dict_day(self): метод для проверки данных прогноза погод по дате.
                + assert указаны:
                    ++ self.assertIsInstance(self.dict_day, dict) проверяем тип
                    ++ проверяем наличие нужных данных в словаре:
                        +++ self.assertIn(temp, i_values) Температура
                        +++ self.assertIn(humidity, i_values) Влажность
                        +++ self.assertIn(pressure, i_values) Давление
                        +++ self.assertIn(wind, i_values) Ветер
                    ++ self.assertIsInstance(datetime.strptime(i_key, format_date), datetime) Проверяем формат даты.
            - def test_error(self): метод для получения данных в случаи ошибки.
                + assert указаны:
                    ++ self.assertTrue(get_weather(city_int), error) получаем в случаи ошибки
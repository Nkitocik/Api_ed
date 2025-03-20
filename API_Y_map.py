import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv('API_KEY')

ADDRESS = input("Геопозицию какого места хотите узнать: ")

URL = f'https://geocode-maps.yandex.ru/1.x/?apikey={API_KEY}&geocode={ADDRESS}&format=json'


response = requests.get(URL)


if response.status_code == 200:
    data = response.json()

    try:
        pos = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
        longitude, latitude = pos.split()
        print(f'Адрес: {ADDRESS}')
        print(f'Координаты: Широта = {latitude}, Долгота = {longitude}')
    except (KeyError, IndexError):
        print('Не удалось найти координаты для указанного адреса.')
else:
    print(f'Ошибка: {response.status_code}')

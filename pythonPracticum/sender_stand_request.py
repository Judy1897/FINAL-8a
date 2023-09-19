import configuration
import requests
import data


# Функция для создания нового заказа:
def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER, json=data.body_order, headers=data.headers)

# Сохранение трека заказа
track = post_new_order().json()["track"]

# Получение заказа по трекеру
def get_order_with_track():
    payload={"t":track}
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER, params = payload)
#print(get_order_with_track().text)

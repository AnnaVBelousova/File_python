"""
2. Задание на закрепление знаний по модулю json. Есть файл orders
в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий
его заполнение данными.

Для этого:
Создать функцию write_order_to_json(), в которую передается
5 параметров — товар (item), количество (quantity), цена (price),
покупатель (buyer), дата (date). Функция должна предусматривать запись
данных в виде словаря в файл orders.json. При записи данных указать
величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json()
с передачей в нее значений каждого параметра.

ПРОШУ ВАС НЕ УДАЛЯТЬ ИСХОДНЫЙ JSON-ФАЙЛ
ПРИМЕР ТОГО, ЧТО ДОЛЖНО ПОЛУЧИТЬСЯ

{
    "orders": []
}

вам нужно подгрузить JSON-объект
и достучаться до списка, который и нужно пополнять
а потом сохранять все в файл
"""

import json

def write_order_to_json(data_dict):
    try:
        with open("orders.json", "r") as f_r:
            orders_list = json.load(f_r)
    except FileNotFoundError:
        orders_list = []
    
    orders_list.append(data_dict)
    
    with open("orders.json", "w") as f_w:
        json.dump(orders_list, f_w, indent=4)
    
    print("Данные добавлены в файл orders.json")

# пример словаря с данными
data_dict = {"item": "bread", "quantity": 2, "price": 25, "buyer": "John", "date": "5.09.22"}

# добавляем данные из словаря в файл json
write_order_to_json(data_dict)

#Данные не добавляются в тот же самый файл json. Создается новый файл

       


"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт,
осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt,
info_3.txt и формирующий новый «отчетный» файл в формате CSV.

Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
с данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список. Должно
получиться четыре списка — например, os_prod_list, os_name_list,
os_code_list, os_type_list. В этой же функции создать главный список
для хранения данных отчета — например, main_data — и поместить в него
названия столбцов отчета в виде списка: «Изготовитель системы»,
«Название ОС», «Код продукта», «Тип системы». Значения для этих
столбцов также оформить в виде списка и поместить в файл main_data
(также для каждого файла);

Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;

Пример того, что должно получиться:

Изготовитель системы,Название ОС,Код продукта,Тип системы

1,LENOVO,Windows 7,00971-OEM-1982661-00231,x64-based

2,ACER,Windows 10,00971-OEM-1982661-00231,x64-based

3,DELL,Windows 8.1,00971-OEM-1982661-00231,x86-based

Обязательно проверьте, что у вас получается примерно то же самое.

ПРОШУ ВАС НЕ УДАЛЯТЬ СЛУЖЕБНЫЕ ФАЙЛЫ TXT И ИТОГОВЫЙ ФАЙЛ CSV!!!
"""





#txt = ['info_1.txt', 'info_2.txt', 'info_3.txt']

"""
Задание на закрепление знаний по модулю CSV. Написать скрипт,
осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt,
info_3.txt и формирующий новый «отчетный» файл в формате CSV.

Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
с данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список. Должно
получиться четыре списка — например, os_prod_list, os_name_list,
os_code_list, os_type_list. В этой же функции создать главный список
для хранения данных отчета — например, main_data — и поместить в него
названия столбцов отчета в виде списка: «Изготовитель системы»,
«Название ОС», «Код продукта», «Тип системы». Значения для этих
столбцов также оформить в виде списка и поместить в файл main_data
(также для каждого файла);

Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;

Пример того, что должно получиться:

Изготовитель системы,Название ОС,Код продукта,Тип системы

1,LENOVO,Windows 7,00971-OEM-1982661-00231,x64-based

2,ACER,Windows 10,00971-OEM-1982661-00231,x64-based

3,DELL,Windows 8.1,00971-OEM-1982661-00231,x86-based

Обязательно проверьте, что у вас получается примерно то же самое.

ПРОШУ ВАС НЕ УДАЛЯТЬ СЛУЖЕБНЫЕ ФАЙЛЫ TXT И ИТОГОВЫЙ ФАЙЛ CSV!!!

os_prod_reg = re.compile(r'Изготовитель системы:\s*\S*')
os_prod_list.append(os_prod_reg.findall(data)[0].split()[2])
"""

"""
Задание на закрепление знаний по модулю CSV. Написать скрипт,
осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt,
info_3.txt и формирующий новый «отчетный» файл в формате CSV.

Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
с данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список. Должно
получиться четыре списка — например, os_prod_list, os_name_list,
os_code_list, os_type_list. В этой же функции создать главный список
для хранения данных отчета — например, main_data — и поместить в него
названия столбцов отчета в виде списка: «Изготовитель системы»,
«Название ОС», «Код продукта», «Тип системы». Значения для этих
столбцов также оформить в виде списка и поместить в файл main_data
(также для каждого файла);

Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;

Пример того, что должно получиться:

Изготовитель системы,Название ОС,Код продукта,Тип системы

1,LENOVO,Windows 7,00971-OEM-1982661-00231,x64-based

2,ACER,Windows 10,00971-OEM-1982661-00231,x64-based

3,DELL,Windows 8.1,00971-OEM-1982661-00231,x86-based

Обязательно проверьте, что у вас получается примерно то же самое.

ПРОШУ ВАС НЕ УДАЛЯТЬ СЛУЖЕБНЫЕ ФАЙЛЫ TXT И ИТОГОВЫЙ ФАЙЛ CSV!!!

os_prod_reg = re.compile(r'Изготовитель системы:\s*\S*')
os_prod_list.append(os_prod_reg.findall(data)[0].split()[2])
"""
import csv
import os
import re

lst = ["info_1.txt", "info_2.txt", "info_3.txt"]

#data_dir = "C:\Geekbrains"  


def get_data(lst):
    data = []

    for filename in lst:
        if filename.endswith(".txt"):  
            with open(filename, "r") as file:
                data.append(file.read())
                # print(data)

    manufacturer_list = []
    os_name_list = []
    product_code_list = []
    system_type_list = []

    for item in data:
        # Извлекаем значения параметров с помощью регулярных выражений
        manufacturer = re.search(r'Изготовитель системы:\s*(.*)', item)
        if manufacturer:
            manufacturer_list.append(manufacturer.group(1))

        os_name = re.search(r'Название ОС:\s*(.*)', item)
        if os_name:
            os_name_list.append(os_name.group(1))

        product_code = re.search(r'Код продукта:\s*(.*)', item)
        if product_code:
            product_code_list.append(product_code.group(1))

        system_type = re.search(r'Тип системы:\s*(.*)', item)
        if system_type:
            system_type_list.append(system_type.group(1))

    print(manufacturer_list)
    print(os_name_list)
    print(product_code_list)
    print(system_type_list)

    for item in data:
        main_data = []  
        manufacturer = re.search(r'Изготовитель системы:', item)
        if manufacturer:
            main_data.append(manufacturer.group(0))

        os_name = re.search(r'Название ОС:', item)
        if os_name:
            main_data.append(os_name.group(0))

        product_code = re.search(r'Код продукта:', item)
        if product_code:
            main_data.append(product_code.group(0))

        system_type = re.search(r'Тип системы:', item)
        if system_type:
            main_data.append(system_type.group(0))
            # return main_data
    print(main_data)

    return main_data, manufacturer_list, os_name_list, product_code_list, system_type_list


print(get_data(lst))


def write_to_csv(file_link):
    data = get_data(lst)  

    with open(file_link, mode='w', newline='') as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow(row)
        print(f"Данные успешно записаны в файл {file_link}")


write_to_csv("C:\\Geekbrains\\csv")
'''
# Доступ к файлам через директорию:

import csv
import os
import re

# lst = ["info_1.txt", "info_2.txt", "info_3.txt"]

data_dir = "C:\Geekbrains"  # замените на путь к вашей директории с данными


def get_data(data_dir):
    data = []

    for filename in os.listdir(data_dir):
        if filename.endswith(".txt"):  # предполагаем, что данные хранятся в текстовых файлах
            with open(os.path.join(data_dir, filename), "r") as file:
                data.append(file.read())
                # print(data)

    manufacturer_list = []
    os_name_list = []
    product_code_list = []
    system_type_list = []

    for item in data:
        # Извлекаем значения параметров с помощью регулярных выражений
        manufacturer = re.search(r'Изготовитель системы:\s*(.*)', item)
        if manufacturer:
            manufacturer_list.append(manufacturer.group(1))

        os_name = re.search(r'Название ОС:\s*(.*)', item)
        if os_name:
            os_name_list.append(os_name.group(1))

        product_code = re.search(r'Код продукта:\s*(.*)', item)
        if product_code:
            product_code_list.append(product_code.group(1))

        system_type = re.search(r'Тип системы:\s*(.*)', item)
        if system_type:
            system_type_list.append(system_type.group(1))

    print(manufacturer_list)
    print(os_name_list)
    print(product_code_list)
    print(system_type_list)

    for item in data:
        main_data = []  # Извлекаем значения параметров с помощью регулярных выражений
        manufacturer = re.search(r'Изготовитель системы:', item)
        if manufacturer:
            main_data.append(manufacturer.group(0))

        os_name = re.search(r'Название ОС:', item)
        if os_name:
            main_data.append(os_name.group(0))

        product_code = re.search(r'Код продукта:', item)
        if product_code:
            main_data.append(product_code.group(0))

        system_type = re.search(r'Тип системы:', item)
        if system_type:
            main_data.append(system_type.group(0))
            # return main_data
    print(main_data)

    return main_data, manufacturer_list, os_name_list, product_code_list, system_type_list


print(get_data(data_dir))


def write_to_csv(file_link):
    data = get_data(
        data_dir)  # предполагается, что функция get_data() уже написана и возвращает данные в виде списка списков

    with open(file_link, mode='w', newline='') as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow(row)
        print(f"Данные успешно записаны в файл {file_link}")


write_to_csv("C:\\Geekbrains\\csv")
'''
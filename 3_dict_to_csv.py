"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv

one_dict = [{'name': 'Joe', 'age': 23, 'job': 'Python dev', 'hobby': 'sport'},
            {'name': 'Tony', 'age': 45, 'job': 'Normal worker', 'hobby': 'books'},
            {'name': 'Niko', 'age': 18, 'job': 'Student', 'hobby': 'Python'},
            {'name': 'Jerry', 'age': 33, 'job': 'Menager', 'hobby': 'gaming'},
            {'name': 'Rick', 'age': 40, 'job': 'No Job', 'hobby': 'Travels'}, 
]

def main():
    with open('one_dict.csv', 'w', encoding='utf-8') as file:
        fields = ['name', 'age', 'job', 'hobby']
        writer = csv.DictWriter(file, fields, delimiter = ';')
        writer.writeheader()
        
        for person in one_dict:
            writer.writerow(person)

if __name__ == "__main__":
    main()

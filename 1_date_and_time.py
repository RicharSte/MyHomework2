"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
import datetime

def print_days():
    
    time_now = datetime.datetime.now()
    yesterday = datetime.timedelta(days=1)
    mouth_ago = datetime.timedelta(days=30)
    
    print(time_now - yesterday)
    print(time_now)
    print(time_now - mouth_ago)
    

def str_2_datetime(date_string):
    
    in_datetime_format = datetime.datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
    
    print(in_datetime_format)
    

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))

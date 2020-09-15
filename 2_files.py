"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    with open('referat.txt', 'r', encoding='utf-8') as file:
        
        sumbols = 0
        words = 0
        
        for line in file:
            sumbols += len(line)
            words += len(line.split())
            
        print(f"Слов - {words} , символов - {sumbols}")
    
    with open('referat2.txt', 'w', encoding='utf-8') as file1:
        with open('referat.txt', 'r', encoding='utf-8') as file2:
            
            for line in file2:
                line = line.replace('.','!')
                file1.write(line)
        
        

if __name__ == "__main__":
    main()

 
# ЗАДАЧА 3 - Своя хеш-функция и словарь
 
import re

class MyHashTable:

    #хеш-таблица с методом цепочек
    
    def __init__(self, size=1000):
        self.size = size
        self.table = [[] for _ in range(size)]  # список списков
        self.collisions = 0
       
    def my_hash(self, word):
        #хеш-функция - сумма кодов символов по модулю размера таблицы
        return sum(ord(c) for c in word) % self.size
    
    def add(self, word):
        """
        Добавление слова в таблицу.
        Если бакет уже содержит другие слова — считаем коллизию
        """
        index = self.my_hash(word)
        
        if len(self.table[index]) > 0 and word not in self.table[index]:
            self.collisions += 1
        
        if word not in self.table[index]:
            self.table[index].append(word)
    
    
    def check(self, word):
        #Проверка наличия слова.
        index = self.my_hash(word)
        return word in self.table[index]
 
# 3.1 Интерактив

def interactive_mode():
    hash_table = MyHashTable()
    
    print("Интерактивный режим запущен.")
    print("Команды: add <слово>, check <слово>, exit")
    
    while True:
        command = input("> ")
        
        if command.startswith("add "):
            word = command[4:]
            hash_table.add(word)
        
        elif command.startswith("check "):
            word = command[6:]
            if hash_table.check(word):
                print("yes")
            else:
                print("no")
        
        elif command == "exit":
            break
    
    print("Количество коллизий:", hash_table.collisions)

# 3.2 Анализ коллизий на тексте

def analyze_collisions(filename):
    """
    Загружает текст, добавляет все слова в хеш-таблицу
    и выводит количество коллизий
    """
    
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()
    
    # извлекаем только слова
    words = re.findall(r"[a-zA-Zа-яА-Я]+", text)
    words = [w.lower() for w in words]
    
    hash_table = MyHashTable(size=1000)
    
    for word in words:
        hash_table.add(word)
    
    print("Всего слов в тексте:", len(words))
    print("\nКоличество коллизий:", hash_table.collisions)
    
    # сравнение с "идеальной" функцией

    unique_words = len(set(words))

    if hash_table.size >= unique_words:
        ideal_collisions = 0
    else:
        ideal_collisions = unique_words - hash_table.size

    print("Минимально возможные (идеальные):", ideal_collisions)
 

if __name__ == "__main__":
    
    print("Выберите режим:")
    print("1 - Интерактивный режим (3.1)")
    print("2 - Анализ текста (3.2)")
    
    choice = input("Введите 1 или 2: ")
    
    if choice == "1":
        interactive_mode()
    
    elif choice == "2":
        filename = "СвойПример.txt"
        analyze_collisions(filename)
        
'''
в результате:
    Сравнил фактическое число коллизий с минимально возможным 
    числом коллизий при идеальном равномерном распределении. 
    В моём случае идеал равен 0, а фактически получилось 12

    Чтобы идеал был не нуль - то можно менять размер таблицы (size=1000)

    При тесте на size = 100 - получилось:
    
    Всего слов в тексте: 257
    Количество коллизий: 98
    Минимально возможные (идеальные): 83

'''

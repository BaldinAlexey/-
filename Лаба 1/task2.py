# ЗАДАЧА 2. Интеллектуальный помощник ввода
 
import re
import random
from collections import defaultdict

# 2.1 Преобразование текста в список слов
def text_to_words(filename):
 
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()
    
    # Ищем только слова из букв
    words = re.findall(r"[a-zA-Zа-яА-Я]+", text)
    
    # Приводим к нижнему регистру
    words = [word.lower() for word in words]
    
    return words
 
# 2.2 Построение словаря биграмм
def build_bigram_dictionary(words):
 
    bigrams = defaultdict(list)
    
    for i in range(len(words) - 1):
        first_word = words[i]
        second_word = words[i + 1]
        bigrams[first_word].append(second_word)
    
    return dict(bigrams)

# 2.3 Автодополнение
def autocomplete(bigram_dict):

    # вводится слово, если есть в словаре, генерирует 3-4 слова

    start_word = input("Введите слово: ").lower()
    
    if start_word not in bigram_dict:
        print("Слово не найдено.")
        return
    
    result = [start_word]
    current_word = start_word
    
    for _ in range(3):  # добавляем 3 слова
        if current_word in bigram_dict:
            next_word = random.choice(bigram_dict[current_word])
            result.append(next_word)
            current_word = next_word
        else:
            break
    
    print("Продолжение:", " ".join(result))
 
def main(filename = "text.txt"):

    print("\nЭтап обучения ")
    
    words = text_to_words(filename)
    print("Всего слов:", len(words))
    
    bigram_dict = build_bigram_dictionary(words)
    print("Всего ключей в словаре биграмм:", len(bigram_dict))
    
    print("\n Автодополнение ")
    autocomplete(bigram_dict)

if __name__ == "__main__": 

    print("\nПример из лабы: ")
    filename = "ПримерИзЛабы.txt" 
    main(filename)

    print("\nСвой пример: ")
    filename = "СвойПример.txt" 
    main(filename)
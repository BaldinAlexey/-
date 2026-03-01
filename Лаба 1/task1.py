 
# ЗАДАЧА 1 - Пересечение мультимножеств
 
from collections import Counter

def multiset_intersection(A, B):
    # Подсчитываем количество элементов в каждом списке
    counter_A = Counter(A)
    counter_B = Counter(B)
    
    result = []
    
    # Для каждого элемента берём минимум его появлений
    for element in counter_A:
        if element in counter_B:
            min_count = min(counter_A[element], counter_B[element])
            result.extend([element] * min_count)
    
    return result

A = [1, 2, 2, 3, 4]
B = [2, 2, 2, 3, 5]

print("Пересечение:", multiset_intersection(A, B))
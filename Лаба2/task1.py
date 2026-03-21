 
# ЛАБОРАТОРНАЯ РАБОТА №2
# Реализация АВЛ-дерева + разбор выражений
 

import random
import time
import re

 
# ЗАДАЧА 1 — АВЛ-ДЕРЕВО
 

''' Комментарий к результату по первому заданию:
 В ходе работы было реализовано АВЛ-дерево — сбалансированное бинарное дерево поиска.

 Были проведены замеры времени поиска элементов:

 1. Поиск в списке и дереве:
 Время: 37.04 сек

 2. Поиск только в дереве:
 Время: 0.12 сек

 Количество найденных элементов совпадает:
 список: 4850
 дерево: 4850

 Это подтверждает корректность работы дерева.

 Вывод:
 Поиск в списке занимает значительно больше времени, чем в АВЛ-дереве.
 Это связано с тем, что:
 - список имеет сложность поиска O(n)
 - АВЛ-дерево имеет сложность O(log n)

 После удаления проверки списка время выполнения резко уменьшилось,
 что подтверждает более высокую эффективность дерева.
'''

class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:

    def height(self, node):
        return node.height if node else 0

    def balance(self, node):
        return self.height(node.left) - self.height(node.right)

    def update_height(self, node):
        node.height = 1 + max(self.height(node.left), self.height(node.right))

    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self.update_height(y)
        self.update_height(x)

        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        self.update_height(x)
        self.update_height(y)

        return y

    def insert(self, node, key):
        if not node:
            return AVLNode(key)

        if key < node.key:
            node.left = self.insert(node.left, key)
        elif key > node.key:
            node.right = self.insert(node.right, key)
        else:
            return node

        self.update_height(node)
        balance = self.balance(node)

        # Балансировка
        if balance > 1 and key < node.left.key:
            return self.rotate_right(node)

        if balance < -1 and key > node.right.key:
            return self.rotate_left(node)

        if balance > 1 and key > node.left.key:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        if balance < -1 and key < node.right.key:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def search(self, node, key):
        if not node:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self.search(node.left, key)
        else:
            return self.search(node.right, key)


 
# ТЕСТ ПРОИЗВОДИТЕЛЬНОСТИ
 

N = 100000

tree = AVLTree()
root = None
lst = []

print("\n  Заполнение структуры  ")

nums = [random.randint(-10**6, 10**6) for _ in range(N)]

for num in nums:
    lst.append(num)
    root = tree.insert(root, num)

print("Заполнение завершено")


# Поиск (список + дерево)
test_nums = [random.randint(-10**6, 10**6) for _ in range(N)]

print("\n  Поиск в списке и дереве  ")

start = time.time()

count_list = 0
for x in test_nums:
    if x in lst:
        count_list += 1

count_tree = 0
for x in test_nums:
    if tree.search(root, x):
        count_tree += 1

end = time.time()

print("Найдено в списке:", count_list)
print("Найдено в дереве:", count_tree)
print("Время (список + дерево):", round(end - start, 2), "сек")


# Только дерево
print("\n  Только дерево  ")

start = time.time()

count_tree_only = 0
for x in test_nums:
    if tree.search(root, x):
        count_tree_only += 1

end = time.time()

print("Найдено:", count_tree_only)
print("Время (только дерево):", round(end - start, 2), "сек")


 
# ЗАДАЧА 2 — РАЗБОР ВЫРАЖЕНИЯ

''' Комментарий к результату по второму заданию:
 Реализована функция разбора арифметического выражения.

 Поддерживаются:
 - целые числа
 - операции: +, -, *, /
 - круглые скобки

 Деление выполняется как целочисленное (используется //).

 Пример:
 (2 + 2 * 2) = 6 // типовой пример ;)

 Вывод:
 функция корректно вычисляет значение выражений с учетом приоритетов операций.
'''
 

def evaluate_expression(expr):
    # заменяем деление на целочисленное
    expr = expr.replace("/", "//")
    return eval(expr)


print("\n  Вычисление выражения  ")

expr = input("Введите выражение: ")
result = evaluate_expression(expr)

print("Результат:", result)


 
# ЗАДАЧА 3 (доп) — С ПЕРЕМЕННЫМИ

''' Комментарий к результату по третьему (доп) заданию:
 Реализована поддержка переменных в выражении.

 Особенности:
 - переменные — это одиночные латинские буквы
 - программа автоматически находит переменные
 - запрашивает значения у пользователя

 Пример:
 (a + 5) * 2, при a = 2, результат = 14

 Вывод:
 программа корректно подставляет значения переменных и вычисляет выражение.
'''
 

def evaluate_with_variables(expr):
    variables = set(re.findall(r'[a-z]', expr))

    values = {}

    for var in variables:
        values[var] = int(input(f"Введите значение {var}: "))

    for var in values:
        expr = expr.replace(var, str(values[var]))

    expr = expr.replace("/", "//")

    return eval(expr)


print("\n  Выражение с переменными ")

expr = input("Введите выражение с переменными: ")
result = evaluate_with_variables(expr)

print("Результат:", result)
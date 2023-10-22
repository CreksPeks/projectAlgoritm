# -*- coding: utf-8 -*-
"""Копия блокнота "Задачи по теме "Алгоритмы и структуры данных""

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qBP298c_wZ2AC4L3tdWQdOnTqOy-PVVz

Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6. Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
"""

a = 5
b = 6
print(a&b)
print(a|b)
print(a^b)
print(b<<2)
print(b>>2)

"""Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5)."""

num = int(input())
chet = 0
not_chet = 0
while num > 0:
    if num % 2 == 0:
        chet += 1
    else:
        not_chet += 1
    num = num//10
print(f"четных - {chet} нечетных - {not_chet}")

"""В массиве случайных целых чисел поменять местами минимальный и максимальный элементы."""

import random
from random import randint

n = int(input("длинна:"))
lst = []
num = 0
for i in range(n + 1):
    num = random.randint(0, 100)
    lst.append(num)
print("1:", lst)
a = max(lst)
b = min(lst)

a1 = lst.index(a)
b1 = lst.index(b)

lst[a1], lst[b1] = lst[b1], lst[a1]
print("2:", lst)

"""Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100]. Выведите на экран исходный и отсортированный массивы.
Примечания:
a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных;
b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком. Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

"""

import random

n = int(input("длинна массива:"))
arr =[]
for i in range(n):
    num = random.randint(-100,101)
    arr.append(num)
print("Исходный массив:", arr)

def sortbubble(x):
    for i in range(n-1):
      for j in range(n-i-1):
        if x[j] < x[j+1]:
            x[j], x[j+1] = x[j+1], x[j]
    print("Отсортированный массив:", x)
sortbubble(arr)

"""Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50]. Выведите на экран исходный и отсортированный массивы."""

def merge_sort(array):

    if len(array) <= 1:
        return array

    # необязательное дополненение
    elif len(array) == 2:
        if array[0] > array[1]:
            array[0], array[1] = array[1], array[0]
        return array

    left = merge_sort(array[:len(array) // 2])
    right = merge_sort(array[len(array) // 2:])
    i, j = 0, 0

    while len(left) > i and len(right) > j:
        if left[i] < right[j]:
            array[i + j] = left[i]
            i += 1
        else:
            array[i + j] = right[j]
            j += 1

    while len(left) > i:
        array[i + j] = left[i]
        i += 1
    while len(right) > j:
        array[i + j] = right[j]
        j += 1

    return array


data = [random.uniform(1, 50,) for i in range(8)]
print(data)
merge_sort(data)
print(data)

"""На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
Примечание. Решите задачу при помощи построения графа.

"""

def create_graph(l):
    return [[0 if i >= j else 1 for j in range(l)] for i in range(l)]

def sum_graph(graph):
    result = 0
    for i in graph:
        result += sum(i)
    return result

n = 5 # количество друзей
new_graph = create_graph(n)
print(sum_graph(new_graph))

"""Закодируйте любую строку по алгоритму Хаффмана."""

from collections import Counter


class Node:

    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value


def get_code(root, codes=dict(), code=''):

    if root is None:
        return

    if isinstance(root.value, str):
        codes[root.value] = code
        return codes

    get_code(root.left, codes, code + '0')
    get_code(root.right, codes, code + '1')

    return codes


def get_tree(string):
    string_count = Counter(string)

    if len(string_count) <= 1:
        node = Node(None)

        if len(string_count) == 1:
            node.left = Node([key for key in string_count][0])
            node.right = Node(None)

        string_count = {node: 1}

    while len(string_count) != 1:
        node = Node(None)
        spam = string_count.most_common()[:-3:-1]

        if isinstance(spam[0][0], str):
            node.left = Node(spam[0][0])

        else:
            node.left = spam[0][0]

        if isinstance(spam[1][0], str):
            node.right = Node(spam[1][0])

        else:
            node.right = spam[1][0]

        del string_count[spam[0][0]]
        del string_count[spam[1][0]]
        string_count[node] = spam[0][1] + spam[1][1]

    return [key for key in string_count][0]


def coding(string, codes):
    res = ''

    for symbol in string:
        res += codes[symbol]

    return res


def decoding(string, codes):
    res = ''
    i = 0

    while i < len(string):

        for code in codes:

            if string[i:].find(codes[code]) == 0:
                res += code
                i += len(codes[code])

    return res


my_string = input('Введите строку для сжатия: ')
tree = get_tree(my_string)

codes = get_code(tree)
print(f'Шифр: {codes}')

coding_str = coding(my_string, codes)
print('Сжатая строка: ', coding_str)

decoding_str = decoding(coding_str, codes)
print('Исходная строка: ', decoding_str)

if my_string == decoding_str:
    print('Успешно!')
else:
    print('Ошибка!')
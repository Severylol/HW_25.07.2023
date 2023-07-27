import os
os.system('cls')
def intersection_set(n, m, set1, set2):
    #преобразую пользовательские вводы в множества
    set1 = set(map(int, set1.split()))
    set2 = set(map(int, set2.split()))

    #нахожу пересечение множеств
    intersection = set1.intersection(set2)

    #преобразую результат обратно в список и сортирую его
    result = sorted(list(intersection))
    return result

#получение данных от пользователя
n = int(input("Введите количество элементов первого множества: "))
m = int(input("Введите количество элементов второго множества: "))
set1 = input("Введите элементы первого множества через пробел: ")
set2 = input("Введите элементы второго множества через пробел: ")

#получаю результат пересечения множеств и вывожу его
result = intersection_set(n, m, set1, set2)
print("Числа, которые встречаются в обоих наборах и отсортированы по возрастанию:", result)

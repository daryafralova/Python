#Задача 1: Выведите в консоль все целые числа от 1 до 100.
numbers = list(range(1, 101))
print(numbers)

#Задача 2: Выведите в консоль все целые числа от -100 до 0.
numbers_1 = list(range(-100, 0))
print(numbers_1)

#Задача 3: Выведите в консоль все целые числа от 100 до 1.

numbers_2 = [i for i in range(100, 0, -1)]
print(numbers_2)

#Задача 4: Выведите в консоль все четные числа из промежутка от 1 до 100.
numbers_4 = list(range(0, 101))
print(numbers_4[::2])

#Задача 5: Выведите в консоль все числа кратные трем в промежутке от 1 до 100.
numbers_5 = list(range(1, 101))
print(numbers_5[::2])

#Задача 6: Дан список: [1, 2, 3, 4, 5, 6]  Получите из него два последних элемента: [5, 6]
spisok_1 = [1, 2, 3, 4, 5, 6]
print(spisok_1[-2:])

#Задача 7: Дана некоторая строка: 'abcdeabc' Получите сет ее символов: {'a', 'b', 'c', 'd', 'e'}
stoka_67 = "abcdeabc"
s=set(stoka_67)
print(s)
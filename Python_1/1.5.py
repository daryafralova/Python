#Задача 1: Найдите сумму всех целых чисел от 1 до 100.
a = sum(list(range(1, 101)))
print(a)

#Задача 2: Найдите сумму всех целых четных чисел в промежутке от 1 до 100.
n=0
for i in range(100):
  if i%2==0:
    n += i
print(n)

#Задача 3: Найдите сумму всех целых нечетных чисел в промежутке от 1 до 100.
n=0
for i in range(100):
  if i%2 != 0:
    n += i
print(n)

#Задача 4: Даны два целых числа. Найдите остаток от деления первого числа на второе.
k = int(input("Введите первое число: "))
l = int(input("Введите второе число: "))
print(k % l)

#Задача 5: Дан список: [1, 2, 3, 4, 5, 6] Получите из него каждый второй элемент: [1, 3, 5]
spisok_456 = [1, 2, 3, 4, 5, 6]
print(spisok_456[::2])
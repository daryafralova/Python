#Задача 1: Дан кортеж с числами: (1, 2, 3, 4, 5) Найдите сумму элементов этого кортежа.
test_tuple = (1, 2, 3, 4, 5)
sum_test_tuple= sum(test_tuple)
print(sum_test_tuple)

#Задача 2: Дан список с числами: [1, 2, 3, 4, 5, 6] Увеличьте каждое число из списка на 10 процентов
my_list_3 = [1, 2, 3, 4, 5]
for i in range(len(my_list_3)):
    my_list_3[i] *= 1.1
    print(my_list_3[i])

my_list_3 = [1, 2, 3, 4, 5]
for i in range(len(my_list_3)):
    my_list_3[i] *= 1.1
    print(my_list_3[i])

#Задача 3: Дана строка: 'abcdef' Получите первых три символа этой строки:'abc'
my_stroka = "abcdef"
print(my_stroka[:3])
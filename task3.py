# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

base_num = (map(float, input("Введите числа через пробел:\n").split())) # присваиваем переменной преобразованный список вещ.чисел
# lst = [ 1.1, 1.2, 3.1, 5.0, 10.01]
d = [round(i % 1, 2) for i in base_num if i % 1 != 0] # переменной присваиваем массив дробной части элементов списка
print("Разница между max и min значением дробной части ", max(d) - min(d)) # вывод результата разницы
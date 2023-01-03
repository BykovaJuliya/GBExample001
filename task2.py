#Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
#для всех значений предикат.
def inputNum(x): # создаем фунцию ввода значений
    mas = ["X", "Y", "Z"] 
    a = []
    for i in range(x):
        a.append(input(f"Введите {mas[i]}: "))
    return a


def Predic(x): # функция предикат
    left = not (x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and not x[2]
    result = left == right
    return result


b = inputNum(3)

if Predic(b) == True: #условие
    print("истина") # вывод 
else:
    print("ложь")  
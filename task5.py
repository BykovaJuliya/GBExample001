#Напишите программу, которая принимает на вход координаты двух точек
#и находит расстояние между ними в 2D пространстве.
#пример:
#- A (3,6); B (2,1) -> 5,09
#- A (7,-5); B (1,-1) -> 7,21

def inputNum(x):
    xy = ["X", "Y"]
    a = []
    for i in range(x):
        number = int(input(f"Введите координату по {xy[i]}: "))
        a.append(number)
    return a


def Length(a, b):
    var = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)
    return var


print("Введите координаты А")
pointA = inputNum(2)
print("Введите координаты В")
pointB = inputNum(2)

print(f"Длина отрезка: {format(Length(pointA, pointB), '.2f')}")

// Задайте значение N. Напишите программу, которая выведет все чётные числа в 
//промежутке от N до 1. Выполнить с помощью рекурсии.
//N = 5 -> "4, 2"
//N = 8 -> "8, 6, 4, 2,"
Console.Write("Введите положительное число: ");
int num = int.Parse(Console.ReadLine());
int i = 1;
EvenToLow(num, i);


void EvenToLow(int n, int i)
{
    if (i > n)
    {
        return;
    }
    else 
    {
       if (n%2==0)

        EvenToLow(n, i + 1);
        Console.Write(i + " ");
    }
}

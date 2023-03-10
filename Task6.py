'''Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и 
получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, 
где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, 
т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
Пример:
385916 -> yes
123456 -> no'''
def GetSum(numberUser):
     sum = 0
     while numberUser > 0:
         sum += numberUser % 10
         numberUser //= 10
     return sum
try:
    number = int(input('Введите шестизначный номер билета - '))
    if number < 0:
        print('Введено не допустимое значение')
    elif number > 99999 and number < 1000000:
        firstSum = GetSum(number // 1000)
        secondSum = GetSum(number % 1000)
        if firstSum == secondSum:
            print('Билет счастливый')
        else:
            print('Билет не счастливый')
    else:
        print('Введено не шестизначное число')
except:
    print('Введено не допустимое значение')
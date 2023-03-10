'''Задача 2: Найдите сумму цифр трехзначного числа.
Пример:
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)'''
try:
    number = int(input('Введите целое трехзначное число - '))
    if number < 0:
        number = -number
    sumDigit = str(number)    
    if number > 99 and number < 1000:
        sum = 0
        while number > 0:
            sum += number % 10
            number //= 10
        print(f'Сумма цифр введенного числа: {sumDigit[0]} + {sumDigit[1]} + {sumDigit[2]} = {sum}')
    else:
        print('Введено не трехзначное число')
except:
    print('Введено не допустимое значение')
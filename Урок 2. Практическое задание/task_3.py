"""
Задание 3.	Сформировать из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
то надо вывести число 6843.

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все цифры извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.

Решите через рекурсию. В задании нельзя применять циклы.

Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321
Не забудьте проверить на числе, которое оканчивается на 0.
1230 -> 0321
"""
def number_opposite(num, result_number=''):
    if len(num) == 1:
        print(f'Перевернутое число: {result_number + num}')
    else:
        result_number += str(int(num) % 10)
        num = int(num) // 10
        number_opposite(str(num), result_number)


if __name__ == '__main__':
    number = input('Введите число:')
    number_opposite(number)
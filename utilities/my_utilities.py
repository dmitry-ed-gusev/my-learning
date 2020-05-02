################################################################################
#
#	Library: my_utilities
#
#	Created:  Dmitrii Gusev, 12.04.2020
#	Modified: Dmitrii Gusev, 15.04.2020
#
################################################################################

from random import random
import sys


def average(arr):  # среднее значение а
    arr_sum = sum(arr)  # встроенная функция sum(), которая возвращает сумму элементов переданного ей списка
    return arr_sum / len(arr)


def print_result(arr, minimum, maximum, average_value):
    print('массив: ', arr, '\n')
    print('минимум: ', minimum)
    print('среднее: ', average_value)
    print('максимум: ', maximum)


def init_array(arr_length):
    arr = [0] * arr_length
    for i in range(arr_length):
        arr[i] = (random() * 1)  # задается промежуток до 1
    return arr


def calculate_array(value):
    arr_length = int(value)  # приводим значение к целочисленному
    arr = init_array(arr_length)  # инициализация массива
    print_result(arr, min(arr), max(arr), average(arr))  # печать результатов


def dec2bin(tab):
    if tab > 1:
        text = (sys.argv[1])  # меняю значение переменной
        cool = (float(text))
        print(bin(int(cool)))
    else:
        print("Please, provide a decimal number for conversion...")


if __name__ == '__main__':
    print("It's a library!")

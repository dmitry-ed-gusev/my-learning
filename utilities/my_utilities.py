################################################################################
#
#	Simple math #1
#
#	Created:  Ishkinin Dmitrii, 17.03.2020
#	Modified: Dmitrii Gusev, 12.04.2020
#
################################################################################

from random import random
import sys  # импортируем библиотеку
from utilities.my_utilities import average
from utilities.my_utilities import print_result

# -- функции


def init_array(arr_length):
    arr = [0] * arr_length
    for i in range(arr_length):
        arr[i] = (random() * 1)  # задается промежуток до 1
    return arr


def worker(value):
    arr_length = int(value)  # приводим значение к целочисленному
    arr = init_array(arr_length)  # инициализация массива
    print_result(arr, min(arr), max(arr), average(arr))  # печать результатов


def main_function(args_length):
    if args_length >= 2:  # если значение text > 1
        worker(sys.argv[1])
    elif args_length == 1:
        gav = input("Введите необходимую длинну массива: ")
        m = len(gav)
        if m >= 1:
            worker(gav)
        else:
            print("Необходимо ввести число!")


# -- код скрипта / программы
length = len(sys.argv)  # длинна аргументов (0, если ввести значение, то: 1, ...)
main_function(length)
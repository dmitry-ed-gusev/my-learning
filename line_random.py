################################################################################
#
#	Simple math #1
#
#	Created:  Ishkinin Dmitrii, 17.03.2020
#	Modified: Dmitrii Gusev, 12.04.2020
#
################################################################################

import sys  # импортируем библиотеку
import utilities.my_utilities as utils


def main_function(args_length):
    if args_length >= 2:  # введено 2 и более чисел
        utils.calculate_array(sys.argv[1]) # .calculate_array производит вычесления
    elif args_length == 1:  #введено одно число
        gav = input("Введите необходимую длинну массива: ")
        m = len(gav)  # длинна массива gav
        if m >= 1:
            utils.calculate_array(gav)
        else:
            print("Необходимо ввести число!")


# -- код скрипта / программы
length = len(sys.argv)  # длинна аргументов (0, если ввести значение, то: 1, ...)
main_function(length)

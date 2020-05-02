################################################################################
#
#	Utility from HEXADECIMAL to ECIMAL.
#
#	Created:  Ishkinin Dmitrii, 15.02.2020
#	Modified: 
#
################################################################################

import sys # импортируем библиотеку


def calculate_sum(tab):
	
	if tab > 1: # если значение text > 1
		text = (sys.argv [1]) # меняю значение переменной
		cool = (int(text)) # int - перевод в десятичную, вывод из массива
		print (hex(cool)) # печать "cool" шестнадцатеричном формате
	else:
		print ("Please, provide a decimal number for conversion...")


# -- код скрипта / программы
hold = len(sys.argv)
calculate_sum(hold)
################################################################################
#
#	Utility from ECIMAL to HEXADECIMAL.
#
#	Created:  Ishkinin Dmitrii, 15.02.2020
#	Modified: 
#
################################################################################

import sys # импортируем библиотеку


def calculate_sum(tab):
	
	if tab > 1: # если значение text > 1
		text = (sys.argv [1]) # меняю значение переменной
		cool = int(text, 16) # int - перевод в десятичную и вывод из массива "text", 
		# 16 - перевод из шестнадцатеричной
		print (cool) # печать "cool" в десятичном формате
	else:
		print ("Please, provide a decimal number for conversion...")


# -- код скрипта / программы
hold = len(sys.argv)
calculate_sum(hold)
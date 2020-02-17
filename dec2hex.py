################################################################################
#
#	Utility from HEXADECIMAL to ECIMAL.
#
#	Created:  Ishkinin Dmitrii, 15.02.2020
#	Modified: 
#
################################################################################

import sys # импортируем библиотеку

text = len(sys.argv) # длинна аргументов (0, если ввести значение, то: 1, ...)

if text > 1: # если значение text > 1

	text = (sys.argv [1]) # меняю значение переменной

	cool = (int(text)) # int - перевод в десятичную, вывод из массива

	print (hex(cool)) # печать "cool" шестнадцатеричном формате

else:

	print ("Please, provide a decimal number for conversion...")
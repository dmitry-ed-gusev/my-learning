################################################################################
#
#	Utility from BINARY to DECIMAL.
#
#	Created:  Ishkinin Dmitrii, 13.02.2020
#	Modified: 
#
################################################################################

import sys # импортируем библиотеку

text = len(sys.argv) # длинна аргументов (0, если ввести значение, то: 1, ...)

if text > 1: # если значение text > 1

	text = (sys.argv [1]) # меняю значение переменной

	cool = int(text, 2) # int - перевод в десятичную, .., 2 перевод из двоичной

	print (cool)

else:

	print ("Please, provide a binary number for conversion...")
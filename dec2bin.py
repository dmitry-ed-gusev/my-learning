################################################################################
#
#	Utility from DECIMAL to BINARY.
#
#	Created:  Ishkinin Dmitrii, 07.02.2020
#	Modified: 
#
################################################################################

import sys # импортируем библиотеку

text = len(sys.argv) # длинна аргументов (0, если ввести значение, то: 1, ...)

if text > 1: # если значение text > 1

	text = (sys.argv [1]) # меняю значение переменной

	print (bin(int(text))[2:]) # печать, двоичный код,  , удаляем 2 последних символа
	
else:

	print ("Please, provide a decimal number for conversion...")

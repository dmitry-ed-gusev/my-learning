################################################################################
#
#	Utility from BINARY to DECIMAL.
#
#	Created:  Ishkinin Dmitrii, 13.02.2020
#	Modified: 
#
################################################################################

import sys # импортируем библиотеку


def calculate_sum(tab):
	
	if tab > 1:
		text = (sys.argv [1]) # меняю значение переменной
		cool = int(text, 2)
		print (cool)
	else:
		print ("Please, provide a binary number for conversion...")


# -- код скрипта / программы
hold = len(sys.argv)
calculate_sum(hold)

################################################################################
#
#	Utility from DECIMAL to BINARY.
#
#	Created:  Ishkinin Dmitrii, 13.02.2020
#	Modified: 
#
################################################################################

import sys # импортируем библиотеку


def calculate_sum(tab):
	
	if tab > 1:
		text = (sys.argv [1]) # меняю значение переменной
		cool = (float(text))
		print (bin(int(cool))) # печать, двоичный код (если число целое),  , удаляем 2 последних символа
	else:
		print ("Please, provide a decimal number for conversion...")



# -- код скрипта / программы
hold = len(sys.argv)  # hold равен длинне кортежа
calculate_sum(hold)  # со значением hold выполняется вся функция

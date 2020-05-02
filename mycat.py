################################################################################
#
#	Script mimics system CAT command.
#
#	Created:  Ishkinin Dmitrii, 02.02.2020
#	Modified: 
#
################################################################################

import sys # импортируем библиотеку


def text_read(tab):
	
	if tab > 1:  # если длинна аргументов больше 1, то
		text = open(sys.argv [1])  # открыть длинну аргументов №1
		print (text.read())  # прочитать длинну аргументов
	else:
		print ("Plesase provide a file for printing...") #Пожалуйста, предоставьте файл для печати ...



# -- код скрипта / программы
hold = len(sys.argv)  # hold равен длинне кортежа
text_read(hold)  # со значением hold выполняется вся функция
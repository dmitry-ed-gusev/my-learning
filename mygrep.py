################################################################################
#
#	Script mimics system GREP command.
#
#	Created:  Ishkinin Dmitrii, 18.02.2020
#
#	Modified: 
#
################################################################################

import sys
# coding: utf8

text = len(sys.argv) # общая длинна аргументов

if text == 3:

	link = (sys.argv[1]) # переменная содержащая ссылку на файл

	word = (sys.argv[2]) # переменная содержащая искомое слово

	with open(link) as file: # (c) открыть link в качестве переменной file

		for line in file: # поиск линии со значением переменной file 

			if word in line: # значение word в линии
			
				print(line, end='') # end='' для удаления пробела между строчками

if text == 2: # есть ссылка или искомое слово

	print('Please, enter a search term...')

if text == 1:

	print ('No arguments specified!')
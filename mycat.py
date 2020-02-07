################################################################################
#
#	Script mimics system CAT command.
#
#	Created:  Ishkinin Dmitrii, 02.02.2020
#	Modified: 
#
################################################################################

import sys

text = len(sys.argv) # длинна аргументов

if text > 1: # если длинна аргументов больше 1, то

	text = open(sys.argv [1]) # открыть длинну аргументов №1

	print (text.read()) # прочитать длинну аргументов

else:

	print ("Plesase provide a file for printing...") #Пожалуйста, предоставьте файл для печати ...
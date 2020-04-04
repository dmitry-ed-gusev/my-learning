################################################################################
#
#	Simple math #1
#
#	Created:  Ishkinin Dmitrii, 17.03.2020
#	Modified: 
#
################################################################################

from random import random
import sys # импортируем библиотеку


text = len(sys.argv) # длинна аргументов (0, если ввести значение, то: 1, ...)

if text > 1: # если значение text > 1

	n = int(sys.argv [1]) # меняю значение переменной

	def average(a): # среднее значение а
		s = sum(a) # встроенная функция sum(), которая возвращает сумму элементов переданного ей списка
		return s/n 
 
	arr = [0] * n
	for i in range(n):
		arr[i] = (random() * 1) # задается промежуток до 1

	f = min(arr)
	z = max(arr)
	b = average(arr)
	print(arr)
	print ('\n')
	print(f, b, z)

else:
	print ("Необходимо ввести число значей!")
	
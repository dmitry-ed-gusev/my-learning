################################################################################
#
#	Simple math #1
#
#	Created:  Ishkinin Dmitrii, 17.03.2020
#	Modified: 
#
################################################################################

from random import random

N = 7 # колличество значений в списке
 
def average(a): # среднее значение а
    s = sum(a) # встроенная функция sum(), которая возвращает сумму элементов переданного ей списка
    return s/N 
 
arr = [0] * N
for i in range(N):
    arr[i] = (random() * 1) # задается промежуток до 1

f = min(arr)
z = max (arr)
b = average(arr)
print(arr)
print ('\n')
print(f, b, z)

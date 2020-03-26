################################################################################
#
#	Utility Eratosthenes lattice.
#
#	Created:  Ishkinin Dmitrii, 26.03.2020
#	Modified: 
#
################################################################################

L = list(range(2, 100)) # решетка Эратосфена
for x in L:
   for y in L[x:]:
      if y % x == 0:        
         L.remove(y)
print(L)
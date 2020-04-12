################################################################################
#
#	Utility sieve of Eratosthenes.
#
#	Created:  Ishkinin Dmitrii, 26.03.2020
#	Modified: 
#
################################################################################

# решето Эратосфена

L = list(range(2, 100))
for x in L:
   for y in L[x:]:
      if y % x == 0:        
         L.remove(y)
print(L)


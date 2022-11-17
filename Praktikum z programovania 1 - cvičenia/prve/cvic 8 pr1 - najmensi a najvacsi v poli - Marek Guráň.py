# cvicenie 8, príklad 1, Marek Guráň
import random
from random import randrange
res = []
def Rand(start, end, num): 
	#res = [] 

	for j in range(num): 
		res.append(random.randint(start, end))

	return res 
 
num = 20
start = 0
end = 20
print(Rand(start, end, num))
print('Maximum v poli je:', max(res), '\nMinimum v poli je:', min(res))

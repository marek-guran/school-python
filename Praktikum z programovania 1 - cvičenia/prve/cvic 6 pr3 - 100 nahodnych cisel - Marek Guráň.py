#cvicenie 6, priklad 3, Marek Guráň
import random

afile = open("Random.txt", "w+" )

for i in range(int(input('Koľko náhodných čísel?: '))):
    line = str(random.randint(1, 100))
    afile.write(line)
    print(line)

afile.close()

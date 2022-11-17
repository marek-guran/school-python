#cvicenie 6, priklad 2, Marek Guráň
#Súbor neskopíruje lebo python nemá práva vytvárať
#súbory v systémovom priečinku a vyhodí iba chybu
#permission error
#je potrebné zapnúť python ako správcu a správca musí
#mať prístup k úplne všetkým povoleniam vo windowse
#ziskavanie uplne vsetkych prav trva od 20 do 50 minút


from shutil import copyfile
from sys import exit

source = input("Zadajte cestu, kde je súbor na skopírovanie: ")
target = input("Zadajte cestu kam chcete uložiť: ")

try:
    copyfile(source, target)
except IOError as e:
    print("Nebolo možné skopírovať súbor. %s" % e)
    exit(1)
except:
    print("Neočakávaná chyba:", sys.exc_info())
    exit(1)

print("\nSkopírovanie dokončené!\n")

while True:
    print("Prajete si vytlačiť súbor? (y/n): ")
    check = input()
    if check == 'n':
        break
    elif check == 'y':
        file = open(target, "r")
        print("\nObsah súboru:\n")
        print(file.read())
        file.close()
        print()
        break
    else:
        continue

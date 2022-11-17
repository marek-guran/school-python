#Hod kockou, Marek Guráň
#nevedel som prísť na to ako spočítať počet hodov pokiaľ nepadne číslo 6

import random
print('Zadávajte gramaticky správne slová áno a nie')
game_start = input("Prajete si hodiť kockou?(áno,nie):")

def dice_roll():
    print("Spadlo číslo: " + str(random.randint(1,6)))
    global play_again
    play_again = input("Prajete si hodiť kockou znova?(áno,nie):")

if game_start == "áno":
    dice_roll()
    while play_again == "áno":
        dice_roll()
elif game_start == "nie":
    print("Koniec hry")
else:
    print("Zle zadaná hodnota áno alebo nie")

if play_again == 'nie':
    print("Koniec hry")

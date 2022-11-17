import matplotlib.pyplot as plt

data1 = open("DJI.txt", "r")
data2 = open("EUUS.txt", "r")


pole1 = list(map(float, data1))
pole2 = list(map(float, data2))

DJI = [0]
DJI.extend(pole1)

EUUS = [0]
EUUS.extend(pole2)

def dji():
    print('Hodnoty akcíí DJI:', DJI)

def euus():
    print('Hodnoty akcií EUUS:', EUUS)

def pokles_DJI():
    pokles = (0)
    stupanie = (0)
    for i in range(250):
        if pole1[i] < pole1[i+1]:
            if pole1[i+1] < pole1[i+2]:
                stupanie = stupanie + 1
            elif pole1[i+1] > pole1[i+2]:
                pokles = pokles + 1
    print('Akcie DJI klesli: ',pokles, 'krát.')
    print('Akcie DJI stúpli: ',stupanie, 'krát.')
            

def pokles_EUUS():
    pokles = (0)
    stupanie = (0)
    for i in range(250):
        if pole2[i] < pole2[i+1]:
            if pole2[i+1] < pole2[i+2]:
                stupanie = stupanie + 1
            elif pole2[i+1] > pole2[i+2]:
                pokles = pokles + 1
    print('Akcie EUUS klesli: ',pokles, 'krát.')
    print('Akcie EUUS stúpli: ',stupanie, 'krát.')
    

def dji_graf():
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251]
    y = DJI

    plt.plot(x, y, color='green', linewidth = 1,
             marker='o', markerfacecolor='blue', markersize=3)

    plt.ylim(31000,38000)
    plt.xlim(0,252)

    plt.xlabel('Deň')
    plt.ylabel('Hodnota akcií')
    plt.title('Dow Jones Industrial Trhová Hodnota')
    plt.show()

def euus_graf():
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251]
    y = EUUS

    plt.plot(x, y, color='green', linewidth = 1,
             marker='o', markerfacecolor='blue', markersize=3)

    plt.ylim(1,2)
    plt.xlim(0,252)

    plt.xlabel('Deň')
    plt.ylabel('Hodnota akcií')
    plt.title('EUUS Trhová Hodnota')
    plt.show()

vyber = 87

while True:
    print()
    print('Výpis hodnôt akcií DJI............................1')
    print('Zobraziť dni koľkokrát kleslo a stúplo DJI........2')
    print('Graf DJI..........................................3')
    print('Výpis hodnôt akcií EUUS...........................4')
    print('Zobraziť dni koľkokrát kleslo a stúplo EUUS.......5')
    print('Graf EUUS.........................................6')
    print('Koniec............................................0')
    print()

    vyber = int(input('Váš výber: '))
    
    
    if vyber == 1:
        dji()
    elif vyber == 2:
        pokles_DJI()
    elif vyber == 3:
        dji_graf()
    elif vyber == 4:
        euus()
    elif vyber == 5:
        pokles_EUUS()
    elif vyber == 6:
        euus_graf()
    elif vyber == 0:
        print('Program bol ukončený.')
        break
    else:
        print('Zlý vstup.')

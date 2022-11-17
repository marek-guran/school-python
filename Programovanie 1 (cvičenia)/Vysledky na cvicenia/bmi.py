#BMI
def bmi(vs,vh):
    ret=''
    bmi=vh/(vs*vs)

    if bmi <18.5:
        ret='podvaha'
    elif 18.5 <=  bmi < 25:
        ret='priemer'
    elif 25 <=  bmi < 30:
        ret='nadvaha'
    else:
        ret='obezita'
    return (bmi,ret)

#Hlavny Program
ntica=()
while True:
    vyska = float(input('Zadajte vysku: '))
    vaha = float(input('Zadajte vahu: '))

    if vyska==vaha==0:
        break
    else:
        ntica=bmi(vyska,vaha)
        print('BMI cloveka je ',ntica[0],', ',ntica[1])
    


    

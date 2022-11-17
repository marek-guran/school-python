#priemerna vyska ziakov
num = int(input('Počet žiakov: '))
total_sum = 0
for n in range(num):
    numbers = float(input('Výška žiaka: '))
    total_sum += numbers
avg = total_sum/num
print('Priemerná výška', num, 'žiakov je:', avg, 'cm')

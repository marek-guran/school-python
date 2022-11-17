#Program na vypocet casu a spotreby vozidla pri prejazde drahy s
s=int(input('Zadajte drahu v metroch: '))
v=100
s=s/1000
t=s/100
print('Auto prejde drahu za ',t*3600,' sekund.')
x=(7200*s)/100
print('Auto spotrebuje ',x*1000,' ml benzinu.')

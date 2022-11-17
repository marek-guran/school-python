#vykreslenie trojuholnika hviezdičkami, Marek Guráň
print('Program na vykreslenie rovno ramenného trojuholníka v hviezdičkách')
rows = input("Zadajte počet stĺpcov:")
rows = int (rows)

for i in range (0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')

    print("\r")

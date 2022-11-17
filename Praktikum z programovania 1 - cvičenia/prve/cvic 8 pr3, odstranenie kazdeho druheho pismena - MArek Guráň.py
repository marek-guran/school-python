#cvicenie 8, príklad 3, MArek Guráň
ret='ABCDEFGH'
new_ret = ""
count = 0
for c in ret:
    if count % 2 == 0:
        new_ret += c
    count += 1
print(new_ret)

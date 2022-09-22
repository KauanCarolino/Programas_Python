s = 0
for n in range(1, 501):
    print(n)
    if n % 2 != 0:
        if n % 3 == 0:
            s += n
print('A soma dos números ímpares múltiplos de 3 é {}'.format(s))

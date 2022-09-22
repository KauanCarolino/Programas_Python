n = int(input('Verificar se é primo: '))
mult = 0

for c in range(2, n):
    if (n % c == 0):
        mult += 1
if (mult == 0):
    print('O número {} é primo'.format(n))
else:
    print('O número {} não é primo'.format(n))

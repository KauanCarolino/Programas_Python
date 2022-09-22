num = int(input("Digite um número: "))
resultado = num % 2
if resultado == 0:
    print("\033[1;32mSeu número {} é par!".format(num))
else:
    print("\033[1;31mSeu número {} é Ímpar!".format(num))

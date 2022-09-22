print("\033[1;33m-=-" * 20)
print("\033[1;33mANALISADOR DE TRIÂNGULOS")
print("\033[1;33m-=-" * 20)
l1 = float(input("Digite o primeiro segmento do triângulo: "))
l2 = float(input("Digite o segundo segmento do triângulo: "))
l3 = float(input("Digite o terceiro segmento do triângulo: "))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print("\033[1;32mOs lados indicados podem formar um triângulo!", end='')
    if l1 == l2 == l3:
        print('EQUILÁTERO')
    if l1 != l2 != l3 != l1:
        print('ESCALENO')
    else:
        print('ISÓCELES')
else:
    print("\033[1;31mOs lados indicados não podem formar um triângulo! :(")
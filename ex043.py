p = float(input('Informe o seu peso em kg: '))
h = float(input('Informe a sua altura em metros: '))
print(' ')
IMC = p / h ** 2

print('Esse é o seu Índice de Massa Corpórea {:.2f}'.format(IMC))

if IMC < 18.5:
    print('Você está Abaixo de Peso!')
elif 18.5 <= IMC < 25:
    print('Você está no Peso ideal!')
elif 25 <= IMC < 30:
    print('Você está comm Sobrepeso!')
elif 30 <= IMC < 40:
    print('Você está com Obesidade!')
elif IMC >+ 40:
    print('Você está com Obesidade Mórbida!')

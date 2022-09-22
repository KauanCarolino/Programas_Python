from time import sleep
cores = {'Limpo': '\033[m',
         'Azul': '\033[1:34m',
         'pretoebranco': '\033[30m',
         'Verde': '\033[1:32m',
         'Vermelho': '\033[1:31m',
         'Ciano': '\033[1:36m'}

print('{}-=-{}'.format(cores['Azul'], cores['Limpo']) * 20)
print("{}Calculador de empréstimos bancário, para comprar uma casa{}".format(cores['Azul'], cores['Limpo']))
print('{}-=-{}'.format(cores['Azul'], cores['Limpo']) * 20)

casa = float(input("Informa o valor da casa: R$"))
salario = float(input("Informe o seu salário: R$"))
anos = int(input("Em quantos anos que vai parcelar: "))

pres = casa / (anos * 12)
minimo = salario * 30 / 100
print("{}CALCULANDO...{}".format(cores['Ciano'], cores['Limpo']))
sleep(2)

print("O valor de prestações mensais é {}R${:.2f} em {} anos {}".format(cores['Ciano'], pres, anos, cores['Limpo']))

if pres <= minimo:
    print("{}Está tudo certo, você pode financiar essa casa!{}".format(cores['Verde'], cores['Limpo']))
else:
    print("{}Bem... Você não pode financiar essa casa{}".format(cores['Vermelho'], cores['Limpo']))

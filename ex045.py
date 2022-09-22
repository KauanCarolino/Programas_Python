from random import choice  # A biblioteca que vai gerar os número
from time import sleep
lista = ['Pedra', 'papel', 'tesoura']

print('Olá, vamos jogar pedra, papel e tesoura!')
print('''As regras são as seguintes:
      -Pedra ganha de tesoura e perde para papel
      -Papel ganha de pedra e perde para tesoura
      -tesoura ganha de papel e perde para pedra
      ''')

player = str(input('Você escolhe pedra, papal ou tesoura? ')).lower()

print('Pedra')
sleep(0.50)
print('Papel')
sleep(0.50)
print('Tesoura')
sleep(0.50)

computador = choice(lista)
vencedor = ""
print('Jogador: {} e computador: {}'.format(player, computador))

if player != str("pedra") and player != str("papel") and player != str("tesoura"):
    print('{} não é uma opção válida. Escolha pedra, papel ou tesoura.'.format(player))
elif player == computador:
    print('Empate. Vamos jogar novamente.')

elif player == "pedra" and computador == "tesoura":
    print('Pedra vence tesoura. O Jogador ganhou!')
elif player == "tesoura" and computador == "pedra":
    print('Pedra vence tesoura. O Computador ganhou!')

elif player == "papel" and computador == "pedra":
    print('Papel ganha de pedra. O Jogador ganhou!')
elif player == "pedra" and computador == "papel":
    print('Papel ganha de pedra. O Computador ganhou!')

elif player == "tesoura" and computador == "papel":
    print('Tesoura ganha de papel. O Jogador ganhou!')
elif player == "papel" and computador == "tesoura":
    print('Tesoura ganha de papel. O Computador ganhou!')

elif player == "tesoura" and computador == "pedra":
    print('tesoura perde para pedra. O perdeu!')
elif player == "tesoura" and computador == "pedra":
    print('Tesoura perde para pedra. O Computador ganhou!')
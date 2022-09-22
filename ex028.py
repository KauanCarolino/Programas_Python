from random import randint  # A biblioteca que vai gerar os número
from time import sleep  # A mensagem de carrega

computer = randint(0, 5)  # O computador vai pensar
print("\033[1;33m-=-\033[m" * 20)
print("\033[1;33mVou pensar em um número entre 0 e 5! Tente adivinhar...\033[1;33m")
print("\033[1;33m-=-\033[m" * 20)
player = int(input("Em que número eu pensei? "))  # O jogador vai tentar adivinhar
print("\033[1;36m PROCESSANDO...\033[m")  # Mensagem de carregamento
sleep(5)  # Tempo de espera para a que apareça a resposta
if player == computer:
    print("\033[7;32;40mVocê acertou!\033[m")
else:
    print("\033[7;31;40mVocê errou! Eu pensei no número {} e não no número {}\033[m".format(computer, player))

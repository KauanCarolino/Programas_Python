import random
a1 = input("Digite o nome do Aluno1: ")
a2 = input("Digite o nomw do Aluno2: ")
a3 = input("Digite o nome do Aluno3: ")
a4 = input("Digite o nome do Aluno4: ")
lista = [a1, a2, a3, a4]
sorteio = random.choice(lista)
print("O aluno sorteado é \033[1;35m{}".format(sorteio))
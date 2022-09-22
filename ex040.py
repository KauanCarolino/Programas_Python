n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

m = (n1 + n2) / 2

if m < 5:
    print('\033[1;31mA média é de {} e o Aluno está REPROVADO \033[m'.format(m))
if 7 > m >= 5:
    print('\033[1;33mA média é de {} e o Aluno está de RECUPERAÇÃO \033[m'.format(m))
elif m >= 7:
    print('\033[1;32mA média é de {} e o Aluno está APROVADO \033[m'.format(m))


from datetime import date

ano_atual = date.today().year
ano = int(input('Informe o seu ano de nascimento: '))

idade = ano_atual - ano

print('Quem nasceu no ano de {}, tem {} anos no ano de {}'.format(ano, idade, ano_atual))

if idade < 18:
    print('Você ainda não está pronto para se alistar nas Forçar Armadas!')
    j = 18 - idade
    print('Daqui a {} anos, você poderá se alistar.'.format(j))
    ano2 = ano_atual + j
    print('Seu alistamento será em {}'.format(ano2))
if idade == 18:
    print('Você já está pronto para se alistar nas Forçar Armadas!')
if idade > 18:
    print('Você já passou da hora de se alistar nas Forças Armadas!')
    a = idade - 18
    print('Você deveria ter se alistado a {} anos.'.format(a))
    ano3 = ano_atual - a
    print('Seu alistamento foi em {}'.format(ano3))

from datetime import date

ano_atual = date.today().year

ano = int(input('Informe o ano de Nascimento do Atleta: '))

idade = ano_atual - ano

print('O Atleta que nasceu no ano de {}, tem {} anos no ano de {}'.format(ano, idade, ano_atual))

if idade <= 9:
    print('Categoria Mirim!')
elif idade <= 14:
    print('Categoria Infantil!')
elif idade <= 19:
    print('Categoria Junior!')
elif idade <= 25:
    print('Categoria Sênior!')
else:
    print('Categoria Master!')

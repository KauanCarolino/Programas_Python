valor = float(input('Informe o preço do produto: '))

print('Qual será a sua forma de pagamento?')
print('Digite 1 para Dinheiro ou cheque.')  # Caso escolha esse você terá 10% de desconto.
print('Digite 2 para á vista no cartão.')  # Caso escolha esse você terá 5% de desconte.
print('Digite 3 para em até 2x no cartão.')  # Caso escolha esse você vai pagar o preço normal.
print('Digite 4 para 3x ou mais no cartão.')  # Caso escolha esse você terá 20% de juros
forma = int(input('Qual dua forma de pagamento? '))

if forma == 1:
    print('O senhor escolheu pagar com Dinheiro ou cheque.')
    desconto = valor - (valor * (10 / 100))
elif forma == 2:
    print('O senhor escolheu pagar no à vista no cartão.')
    desconto = valor - (valor * (5 / 100))
elif forma == 3:
    print('O senhor escolheu pagar em até 2x no cartão.')
    desconto = valor
    parcela = desconto / 2
    print('Sua compra será parcelada de 2x de {:.2f} sem juros'.format(parcela))
elif forma == 4:
    print('O senhor escolheu pagar em 3x ou mais no cartão.')
    desconto = valor + (valor * (20 / 100))
    toparc = int(input('Em quantas vezes você deseja parcelar? '))
    parcelas = desconto / toparc
    print('Sua compra será parcelada em {}x de R${:.2f} com juros'.format(toparc, parcelas))
print('Sua compra de R${:.2f} ao final vai custar R${:.2f}'.formart(valor, desconto))

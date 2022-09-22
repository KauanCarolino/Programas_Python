s = float(input("Qual o salário do funcionário? R$"))

novo = s + (15 / 100 * s)

print("O seu salário era de R${:.2f}, com 15% de aumento, será de R${:.2f}  ".format(s, novo))
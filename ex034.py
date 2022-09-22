money = float(input("Digite o salário do funcionário: R$"))
if money >= 1250:
    S = money + (10 / 100 * money)
    print("O seu novo salário será de R${:.2f}".format(S))
if money <= 1250:
    s = money + (15 / 100 * money)
    print("O seu novo salário será de R${:.2f}".format(s))

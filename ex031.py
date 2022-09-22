km = float(input("\033[1;33mQual a distância da sua viagem em km? "))
print("\033[1;33mPara uma viagem de {}km".format(km))
if km >= 201:
    p2 = (km * 0.45)
    print("\033[1;35mO custo da sua Passagem será de R${:.2f}".format(p2))
else:
    p = (km * 0.50)
    print("\033[1;36mO custo da sua passagem será de R${:.2f}".format(p))

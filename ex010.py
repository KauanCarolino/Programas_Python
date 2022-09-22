din = float(input("Quanto dinheiro você tem na carteira? R$"))
dol = din / 5.17
eur = din / 6.13
print("Com R$\033[4;32m{:.2f}\033[m você pode comprar US$\033[4;31m{:.2f}\033[m".format(din, dol))
print("Com R$\033[4;32m{:.2f}\033[m você pode comprar €\033[3;31m{:.2f}\033[m".format(din, eur))

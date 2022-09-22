km = float(input("Quantos Km rodados? "))
d = int(input("Quantos dias alugados? "))

dist = (km * 0.15)
dias = (d * 60)
t = (dist + dias)
print("O total a pagar é de {:.2f}R$".format(t))
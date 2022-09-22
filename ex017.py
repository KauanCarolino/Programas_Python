from math import hypot
co = float(input("Digite o cateto oposto: "))
ca = float(input("Digite o cateto adjacente: "))
hi = hypot(co, ca)
print("A soma dos catetos co {} e ca {} é a hip {:.2f}".format(co, ca, hi))

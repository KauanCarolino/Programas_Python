p = float(input("Insira o preço do produto? R$ "))

np = p - (5 / 100 * p)

print("O seu produto que custava R${:.2f}, com 5% de desconto custará R${:.2f}".format(p, np))
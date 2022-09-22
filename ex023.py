num = int(input("\033[4;34mDigite um número:\033[m "))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print("Analisando o número \033[1;35m{}".format(num))
print("Unidades: \033[1;35m{}".format(u))
print("Dezenas: \033[1;35m{}".format(d))
print("Centenas: \033[1;35m{}".format(c))
print("Dezenas: \033[1;35m{}".format(m))

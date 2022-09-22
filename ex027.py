nome = str(input("\033[1;33mDigite seu nome completo: ")).strip()

n = nome.split()

print("O seu primeiro nome é {}".format(n[0]))
print("O seu último nome é {}".format(n[len(n)-1]))

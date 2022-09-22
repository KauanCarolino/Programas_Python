nome = input("Digite seu nome completo: ").strip()

primeiro = nome.split()

print("O nome em maiúsculas é: ",nome.upper())
print("O nome em minúsculas é: ",nome.lower())
print("O seu nome tem o total de {} letras".format((len(nome.replace(" ", "")))))
print("O seu primeiro nome tem {} letras".format(len(primeiro[0])))

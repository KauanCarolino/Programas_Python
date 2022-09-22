primeiro = int(input("Digite o primeiro número: "))
segundo = int(input("Digite o segundo número: "))
terceiro = int(input("Digite o terceiro número: "))
# Verificando o Maior
maior = primeiro
if segundo > maior:
    maior = segundo
if terceiro > maior:
    maior = terceiro
print("O maior número é {}: ".format(maior))
# Verificando o menor
menor = primeiro
if segundo < menor:
    menor = segundo
if terceiro < menor:
    menor = terceiro
print("O menor número é {}: ".format(menor))

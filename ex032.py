from datetime import date
ano = int(input("\033[1;34mQue ano você quer analisar? Coloque 0 para analisar o ano atual: \033[m"))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("\033[1;33mO ano de {} é Bissexto!\033[m".format(ano))
else:
    print("\033[1;36mO ano de {} não é bissexto!\033[m".format(ano))


'''from calendar import isleap
ano = int(input("Que ano você quer analisar? "))
if not isleap(ano):
    print("Não é um ano Bissexto!")
else:
    print("É um ano bissexto!")'''
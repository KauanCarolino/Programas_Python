vel = float(input("QUal a velocidade do seu carro? "))

if vel > 80:
    print("\033[1;31mVocê está acima da velocidade permitida que é de 80km/h")
    multa = (vel - 80) * 7
    print("Você deve pagar uma multa de R$\033[1;31m{:.2f}".format(multa))
else:
    print("\033[7;32;40mVocê está na velocidade permitida! Tenha um bom dia e dirija com segurança!\033[m")

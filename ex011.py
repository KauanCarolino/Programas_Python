larg = float(input("Largura da parede? "))
alt = float(input("Altura da parede? "))

área = larg * alt

print("Sua parede tem as dimensões {}x{} e sua área é de {}m²".format(larg, alt, área))

tinta = área / 2

print ("para pintar essa parede é preciso de {}L de tinta".format(tinta))
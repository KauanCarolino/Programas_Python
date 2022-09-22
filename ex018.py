from math import radians, sin, cos, tan

an = float(input("Digite o seu ângulo: "))

sen = sin(radians(an))
cos = cos(radians(an))
tg = tan(radians(an))

print("O ângulo de {} tem o Seno {:.2F}".format(an, sen))
print("O ângulo de {} tem o Cosseno {:.2F}".format(an, cos))
print("O ângulo de {} tem a Tangente {:.2F}".format(an, tg))
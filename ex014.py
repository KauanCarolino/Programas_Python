t = float(input("\033[2;36mInforme a temperatura em °C: "))
nt = (t * 9/5) + 32
print ("A sua temperatura em \033[1;31m{:.1f}°C\033[m, vale \033[1;31m{:.1f}°F".format(t, nt))
#!/usr/bin/python3

tc = list(input("Digite: "))
tc = [float(i) for i in tc]
resultado_celsius = list(map(lambda tc : float(9/5) * (tc + 32),tc))
resultado_farenheit = list(map(lambda tc : float(5/9) * (tc - 32),tc))

print("A tempetatura em Farenheit é: {} \nA temperatura em Celsius: {} ".format(resultado_farenheit,resultado_celsius))
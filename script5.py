minutos = int(input('Quantos minutos foram utilizados?:'))

if minutos < 200:
    consumo = 0.2
elif minutos <= 400:
    consumo = 0.18
else:
    consumo = 0.18

format('Total: R$ {p} ',p=minutos*consumo)



exit()
minutos  = int(input('Quantos minutos foram utilizados?: '))

if minutos < 200:
    consumo = 0.2
elif minutos <= 400:
    consumo = 0.18
else:
    consumo = 0.15

print('Total: R$ %.2f'%(minutos * consumo))

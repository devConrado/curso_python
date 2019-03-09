#ler 3 numeros de entrada e encontrar o maior
n1 = int(input('Entre com o primeiro numero: '))
n2 = int(input('Entre com o segundo numero: '))
n3 = int(input('Entre com o terceiro numero: '))

if n1 > n2 and n1 > n3:
    print('N1 é o maior número')
elif n2 > n3 and n2 > n3:
    print('N2 é o maior numero')
elif n3 > n2 and n3 > n1:
    print('N3 é o maior')
elif n1 == n2 and n1 == n3 and n2 == n3:
    print('Os tres são iguais !')

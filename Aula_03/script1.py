#!/usr/bin/python3

calcula = {'soma': lambda x,y : x+y, 'subtrai' : lambda x,y : x-y, 'multiplica': lambda x,y : x*y, 'divide': lambda x,y : x/y}
funcao = calcula['soma']
print(funcao(10,15))
print(calcula['soma'](10,15))

exit()

tamanho = lambda palavra : [len(p) for p in palavra]
frase = 'Winter is commig!'.split()
print(frase)
print(tamanho(frase))

exit()

def tamanho(palavra):
	return [len(p) for p in palavra]

frase = 'Ola mundo'. split()
print(frase)
print(tamanho(frase))

exit()

def multiplica(n):
	return lambda a : a * n 

dobro = multiplica(2)
triplo = multiplica(3)

print(dobro(12))
print(triplo(12))

exit()

x = lambda a,b,c : a + b + c
print(x(5,6,10))

exit()

x = lambda a,b : a * b

print(x(10,10))
print(x(10,20))

exit()

x = lambda a : a + 10
print(x(5))
print(x(2))
print(x(10))


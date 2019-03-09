#!/usr/bin/python3

def descobre(**kwargs):
	print =(kwargs)

	for k in kwargs.keys():
		print('chave: {}'.format(k))
		print('valor: {}'.format(kwargs[k]))

descobre(nome='pedro', sobrenome='moura')
descobre(nome='servidor', ip='192.168.0.1', dominio='4linux.com.br')

exit()
#############################################################################################

def calcular(*args):
	if len(args) == 1:
		print('area: ',(args[0]*args[0]))
	elif len(args) == 2:
		print('area: ',(args[0]*args[1]))
	elif len(args) == 3:
		print('volume: ',(args[0]*args[1])*args[2])
	else:
		print('Excedeo o numero limite de argumentos que é no maximo 3')

calcular(2)
calcular(2,8)
calcular(2,5,3)

exit()
#############################################################################################

def animal(tipo='hamster',nome='hantaro'):
	print('eu tenho um {} e se chama {}'.format(tipo,nome))

animal()

exit()
#############################################################################################

def animal(tipo,nome):
	print('eu tenho um {} e se chama {}'.format(tipo,nome))

animal('cachorro', 'rex')

exit()
#############################################################################################
def diga_ola(nome):
	print('ola {}'.format(nome.title()))

def pergunta_nome():
	nome = input('Digite seu nome: ')
	diga_ola(nome)

pergunta_nome()

exit()
#############################################################################################
def diga_ola(nome):
	print('ola {}'.format(nome.title()))

def pergunta_nome():
	nome = input('Digite seu nome: ')
	return nome

n = pergunta_nome()
diga_ola(n)

exit()
#############################################################################################
def diga_ola():
	print('ola {}'.format(nome.title()))

nome = input('Digite o seu nome: ')

diga_ola()
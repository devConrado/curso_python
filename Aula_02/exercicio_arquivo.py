#!/usr/bin/python3
def Cadastrar():
	nome = input('Digite o seu Nome: ')
	estado = input('Digite o seu Estado: ')
	cpf = input('Digite o seu CPF: ')
	with open('arquivo.txt','a') as arquivo:
		arquivo.write('{}\t {}\t {}\t \n'.format(nome,estado,cpf))

def Buscar():
	busca = input('Digite o nome que deseja filtrar: ')
	with open('arquivo.txt') as arquivo:
		l = []
		for linha in arquivo:
			l.append(linha)


print('Selecione uma das opções:')
print('1- Cadastrar Dados')
print('2- Buscar Dados')
op = int(input('Digite a opção: '))

if op == 1:
	Cadastrar()
elif op == 2:
	Buscar()
else:
	print('Opção não encontrada por favor tente outra opção!')





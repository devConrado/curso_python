#!/usr/bin/python3

from conmongo import *

def drop_tabela():
	db.usuarios.drop()
	print('Tabela Dropada!')

def atualizacao():
	while True:
		uid = int(input("Digite o ID: "))
		if str(uid) == 'n':
			busca()
		else:
			break
	print('Selecione o campo:\n1. nome\n2.cpf\n3.estado')
	o = int(input('Digite: '))

	if o == 1:
		nome = input('Digite o novo nome: ')
		db.usuarios.update({'_id':uid},{'$set':{'nome':nome}})
	elif o == 2:
		cpf = input('Digite o novo cpf: ')
		db.usuarios.update({'_id':uid},{'$set':{'cpf':cpf}})
	else:
		estado = input('Digite o novo estado: ')
		db.usuarios.update({'_id':uid},{'$set':{'estado':estado}})


def busca():
	nome = input('Digite o nome: ')
	print([k for k in db.usuarios.find({'nome': nome})])

def cadastro():
	nome = input('Digite o nome: ')
	cpf = input('Digite o cpf: ')
	estado = input('Digite o estado: ')

	lista_seriais = [k['_id'] for k in db.usuarios.find()]
	serial = 1

	for i in lista_seriais:
		if serial == i:
			serial += 1
		else:
			break

	encontrado = [k for k in db.usuarios.find({'cpf':cpf})]

	if encontrado:
		print('Usuario ja existe na base!')
	else:
		db.usuarios.insert({'_id':serial,'nome':nome,'cpf':cpf,'estado':estado})
		serial += 1
		print("Cliente inserido com sucesso")

def delecao():
	while True:
		uid = int(input("Digite o ID: "))
		if str(uid) == 'n':
			busca()
		else:
			break
	db.usuarios.remove({'_id':id})

def sair():
	print('saindo')
	exit()
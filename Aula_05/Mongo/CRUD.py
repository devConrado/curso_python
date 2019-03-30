#!/usr/bin/python3
import conMongo as con

def Find():
	nome = input("Insira o nome para a busca: ")
	con.Find(nome)

def Add():
	nome = input("Insira o Nome: ")
	cpf = input("Insira o CPF: ")
	estado = input("Insira o Estado: ")
	usuario = {'nome': nome, 'cpf': cpf, 'estado': estado}
	con.Add(usuario)

def Update():
	cpfBusca = input("Insira um CPF para a busca: ")
	nome = input("Insira o Nome para atualizar: ")
	cpf = input("Insira o CPF para atualizar: ")
	estado = input("Insira o Estado para atualizar: ")
	usuario = {'nome': nome, 'cpf': cpf, 'estado': estado}
	con.Update(cpfBusca,usuario)

def Delete():
	nome = input("Insira o Nome a ser deletado: ")
	con.Delete(nome)

def DropUsers():
	print("DropUsers")

while True:
	menu = {0 : exit, 1: Find, 2: Add, 3: Update, 4: Delete, 5: DropUsers}
	print("Menu: \n 0. Sair\n 1. Buscar pelo nome\n 2. Cadastrar Usuario\n 3.Alterar Usuario\n 4.Deletar Usuario\n 5.Dropar a Tabela")
	op = int(input("Selecione um opção: "))
	if op > 5 or op < 0 :
		print('Opção Invalida tente outra !')
	else:
		menu[op]()
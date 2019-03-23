#!/usr/bin/python3
import conexao as cn

def selecionar():
	nome = input('\nInsira o Nome: ')
	cn.select(nome)

def atualizar():
	cpf = input('\nInsira o CPF: ')
	cn.update(cpf)

def deletar():
	cpf = input('\nInsira o CPF: ')
	cn.delete(cpf)

def inserir():
	nome = input('\nInsira um Nome: ')
	cpf = input('Insira o CPF: ')
	estado = input('Insira o Estado: ')
	usuario = [nome,cpf,estado]
	cn.insert(usuario)

menu = {'0':exit,'1':selecionar,'2':inserir,'3':atualizar,'4':deletar,'5':cn.createTable,'6':cn.dropTable}

while True:
	print("..:: Menu ::..")
	print("0. Sair")
	print("1. Buscar por nome")
	print("2. Cadastrar")
	print("3. Atualizar")
	print("4. Deletar")
	print("5. Criar a Tabela Usuarios")
	print("6. Dropar a Tabela Usuarios")
	op = input('Selecione a opção: ')
	menu[op]()
exit()
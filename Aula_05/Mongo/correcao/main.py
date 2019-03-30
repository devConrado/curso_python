#!/usr/bin/python3
import os
from funcoes import *

opcoes = {'0':sair,'1':busca,'2':cadastro,'3':atualizacao,'4':delecao,'5':drop_tabela}
menu = "Menu: \n 0. Sair\n 1. Buscar pelo nome\n 2. Cadastrar Usuario\n 3.Alterar Usuario\n 4.Deletar Usuario\n 5.Dropar a Tabela"

while True:
	try:
		os.system('clear')
		print(menu)
		op = input('Digite opcao: ')
		opcoes[op]()
		
	except Exception as e:
		print('Erro {}'.format(e))
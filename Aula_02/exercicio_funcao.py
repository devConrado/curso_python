#!/usr/bin/python3

def caculadora():
	calc = input('Digite a operacao a ser realizada: ')
	o = []
	for c in calc:
		o.append(c)
	if o[1] == '+':
		print('A soma dos números são: {}'.format(int(o[0]) + int(o[2])))
	elif o[1] == '-':
		print('A subtração dos números são: {}'.format(int(o[0]) - int(o[2])))
	elif o[1] == '*':
		print('A multiplicação dos números são: {}'.format(int(o[0]) * int(o[2])))
	elif o[1] == '/':
		print('A divisão dos números são: {}'.format(int(o[0]) / int(o[2])))
	else:
		print('Não foi possivel realizar a operação')

############################################ Resultado ############################################

caculadora()
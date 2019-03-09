#!/usr/bin/python3
def caculadora():
	calc = input('Digite a operacao a ser realizada: ')
	o = []
	for c in calc:
		o.append(c)
	a,b = int(o[0]),int(o[2])
	dicionario = {'+':a+b,'-':a-b,'*':a*b,'/':a/b}
	try:
		z = dicionario[o[1]]
		print('Resultado: {}'.format(z))
	except Exception as e:
		print('Operação Invalida: {}'.format(e))

############################################ Resultado ############################################

caculadora()
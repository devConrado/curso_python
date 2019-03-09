#!/usr/bin/python3

with open('arquivo.txt','a') as arquivo:
	arquivo.write('estou escrevendo o arquivo one more time')

exit()
#############################################################
with open('arquivo.txt','w') as arquivo:
	arquivo.write('estou escrevendo no arquivo')

exit()
#############################################################
with open('arquivo.txt') as arquivo:
	linhas = arquivo.readlines()

string = ''

for linha in linhas:
	string += linha.rstrip()

print(string)

exit()
############################################################
with open('arquivo.txt') as arquivo:
	linhas = arquivo.readlines()
print(linhas)

exit()
############################################################
with open('arquivo.txt') as arquivo:
	for linha in arquivo:
		print(linha)

exit()
############################################################
arquivo = open('arquivo.txt')
print(arquivo.read())
arquivo.close()

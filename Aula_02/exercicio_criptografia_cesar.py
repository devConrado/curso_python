#!/usr/bin/python3
import sys as s
def cifra(mensagem,direcao,chave):
	m = ''
	for c in mensagem:
		if c in dicionario:
			indice = dicionario.index(c)
			m += dicionario[(indice + direcao * chave) % len(dicionario)]
		else:
			m += c
	return m
	
def criptografa(mensagem, chave):
	print(cifra(mensagem,1,chave))
def descriptografa(mensagem,chave):
	print(cifra(mensagem,-1,chave))

o = s.argv
tipo = o[1].lower()
mensagem = o[2].lower()
chave = int(o[3])

opt = {'cript':criptografa, 'descript': descriptografa}
dicionario = ['abcdefghijklmnopqrstuvwxyz']

try:
	opt[tipo](mensagem,chave)
except Exception as e:
	print("comando invalido !")




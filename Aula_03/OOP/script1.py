#!/usr/bin/python3

class Restaurante():
	def __init__(self,nome,tipo,aberto):
		self.nome = nome
		self.tipo = tipo
		self.aberto = aberto

	def descreve(self):
		print ("{} é o restaurante de comida {}".format(self.nome.title(),self.tipo))

	def status(self):
		if self.aberto == True:
			print("{} está aberto".format(self.nome.title()))
		else:
			print("{} está fechado".format(self.nome.title()))

r1 = Restaurante('Habibs','arabe',True)
r1.descreve()
r1.status()

r2 = Restaurante('Outback','australiana',True)
r2.descreve()
r2.status()
r2.aberto = False
r2.status()
#!/usr/bin/python3

class Usuario():

	def __init__(self,nome,sobrenome):
		self.nome = nome
		self.sobrenome = sobrenome

	def descrever(self):
		print("O seu nome é {} {}".format(self.nome, self.sobrenome))

usuario = Usuario("João", "da Silva")
usuario2 = Usuario("Fulano", "Beltrano")
usuario.descrever()
usuario2.descrever()
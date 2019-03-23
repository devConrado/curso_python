#!/usr/bin/python3
class Dog():
	"""docstring descreve sua classe """
	dono = None

	def __init__(self, nome, idade):
		self.nome = nome
		self.idade = idade

	def sentar(self):
		print("{} está sentado agora".format(self.nome.title()))

	def deitar(self):
		print("{} está deitado agora".format(self.nome.title()))

meu_dog = Dog('Jake',2)
meu_dog.dono = "Matheus"
seu_dog = Dog('Ted',10)

print("meu dog tem {} e se chama {} e o seu dono é o {}".format(meu_dog.idade, meu_dog.nome, meu_dog.dono))
print("Seu dog tem {} e se chama {}".format(seu_dog.idade, seu_dog.nome))

meu_dog.sentar()
seu_dog.deitar()
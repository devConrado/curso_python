#!/usr/bin/python3
from pymongo import MongoClient

try:
	con = MongoClient()
	db = con['CRUD']
	print("Conectado!")
except Exception as e:
	print("Erro {}".format(e))

def Find(nome):
	result = db.usuario.find({"nome":nome})
	for k in result:
		print("Nome: {}".format(k['nome']))
		print("CPF: {}".format(k['cpf']))
		print("Estado: {}".format(k['estado']))

def Add(usuario):
	db.usuario.insert({"nome":usuario['nome'],"cpf":usuario['cpf'],"estado":usuario['estado']})
	print("Usuario {} inserido com sucesso!".format(usuario['nome']))

#Passar o nome inserido e o dicionario
def Update(cpf,usuario):
	db.usuario.update({"cpf":cpf},{'$set':{"nome":usuario['nome'],"cpf":usuario['cpf'],"estado":usuario['estado']}})
	print("{} alterado com sucesso".format(usuario['nome']))

def Delete(nome):
	db.usuario.delete({"nome":nome})

def DropUsers():
	print("DropUsers")

Update('Matheus',{'nome':'Matheus','cpf':'01234567890','estado':'SP'})
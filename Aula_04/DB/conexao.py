#!/usr/bin/python3
import psycopg2 as pg

try:
    con = pg.connect('host=localhost dbname=gotham user=batman password=gotham123')
    print('Conectado!')
    c = con.cursor()
except Exception as e:
    print('Erro: {}'.format(e))

def insert(usuario):
	c.execute('insert into Usuario (nome, cpf, estado) values ({},{},{});'.format(usuario[0],usuario[1],usuario[2]))
	c.commit()
	print('Usuario {} salvo com sucesso!'.format(usuario[0]))

def select(nome):
	usuarios = c.fetchall('select * from Usuario where nome = {}'.format(nome))
	for row in usuarios:
		print('Nome: {}'.format(row[1]))
		print('CPF: {}'.format(row[2]))
		print('Estado: {}'.format(row[3]))
		print('\n')

def update(cpf):
	usuarios = c.fetchall('select * from Usuario where cpf = {}'.format(cpf))
	c.execute('update Usuario set nome = {},cpf = {},estado = {} where nome = {};'.format(usuarios[1],usuarios[2],usuarios[3]))
	c.commit()
	print('Usuario {} salvo com sucesso!'.format(usuarios[1]))

def delete(cpf):
	c.execute('delete from Usuario where cpf = {};'.format(cpf))
	c.commit()
	print('Usuario com o CPF {} deletado com sucesso!'.format(usuario[0]))

def createTable():
	c.execute('create table Usuarios(id serial, nome varchar(50), cpf varchar(50), estado varchar(50));')
	c.commit()
	print('Tabela criada com sucesso!')

def dropTable():
	c.execute('drop table Usuario;')
	c.commit()
	print('Tabela dropada com sucesso!')

#!/usr/bin/python3
import psycopg2 as pg

try:
    con = pg.connect('host=localhost dbname=gotham user=batman password=gotham123')
    print('Conectado!')
    c = con.cursor()
except Exception as e:
    print('Erro: {}'.format(e))

def insert(usuario):
	c.execute('insert into Usuarios (nome, cpf, estado) values (\'{}\',\'{}\',\'{}\');'.format(usuario[0],usuario[1],usuario[2]))
	con.commit()
	print('Usuario {} salvo com sucesso!'.format(usuario[0]))

def select(nome):
	c.execute('select * from Usuarios where nome = \'{}\';'.format(nome))
	usuarios = c.fetchall()
	for row in usuarios:
		print('Nome: {}'.format(row[1]))
		print('CPF: {}'.format(row[2]))
		print('Estado: {}'.format(row[3]))
		print('\n')

def update(cpf):
	c.execute('select * from Usuarios where cpf = \'{}\''.format(cpf))
	usuarios = c.fetchall()
	c.execute('update Usuarios set nome = \'{}\',cpf = \'{}\',estado = \'{}\' where nome = \'{}\';'.format(usuarios[1],usuarios[2],usuarios[3]))
	con.commit()
	print('Usuario com o CPF {} salvo com sucesso!'.format(cpf))

def delete(cpf):
	c.execute('delete from Usuarios where cpf = \'{}\';'.format(cpf))
	con.commit()
	print('Usuario com o CPF {} deletado com sucesso!'.format(cpf))

def createTable():
	c.execute('create table Usuarios(id serial, nome varchar(50), cpf varchar(50), estado varchar(50));')
	con.commit()
	print('Tabela criada com sucesso!')

def dropTable():
	c.execute('drop table Usuarios;')
	con.commit()
	print('Tabela dropada com sucesso!')

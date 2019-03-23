#!/usr/bin/python3
import psycopg2 as pg
import psycopg2 as pg

try:
    con = pg.connect('host=localhost dbname=gotham user=batman password=gotham123')
    print('Conectado!')
    c = con.cursor()
except Exception as e:
    print('Erro: {}'.format(e))



try:
	c.execute('create table Usuarios(id serial, nome varchar(50), idade int);')
	con.commit()
	c.execute('insert into viloes (nome, idade) values ("Charada",20);')
	c.execute('insert into viloes (nome, idade) values ("Lex Luthor",37);')
	c.execute('insert into viloes (nome, idade) values ("Pinguim",34);')
except Exception as e:
	print('Erro: {}'.format(e))













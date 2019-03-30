#!/usr/bin/python3

from conexao import user_table, engine

con = engine.connect()
ins = user_table.insert()

#new = ins.values(idade=50, nome='Joao',senha='123')
#con.execute(new)

con.execute(ins,[
	{'nome':'Pedro','idade':'27','senha':'senha123'},
	{'nome':'Maria','idade':'25','senha':'123'},
	{'nome':'Thiago','idade':'37','senha':'sea23'},
	{'nome':'Carlos','idade':'32','senha':'seh123'},
	{'nome':'Lucas','idade':'56','senha':'sena3'}
	])
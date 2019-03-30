#!/usr/bin/python3

from sqlalchemy import update
from conexao import user_table,engine

con = engine.connect()

atualizar = update(user_table).where(user_table.c.nome == 'Maria')
commit = atualizar.values(nome='Priscilla')

result = con.execute(commit)
print(result.rowcount)
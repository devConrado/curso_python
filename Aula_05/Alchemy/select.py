#!/usr/bin/python3

from sqlalchemy import select
from conexao import user_table,engine

result = select([user_table])
print(result.execute())

#for k in result.execute():
#	print(k)

#print([k for k in result.execute()])

print([k for k in select([user_table]).where(user_table.c.nome == 'Joao').execute()])
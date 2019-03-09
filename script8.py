viloes = ['lex luthor','coringa','alerquina','duas caras','sinistro','darkseid']

vilao = 'thanos'

if vilao in viloes:
    print(vilao.title() + ' ta na lista')
else:
    print(vilao.title() + ' não ta na lista')
    viloes.append(vilao)

print(viloes)

for vilao in viloes:
    print('{} e muito mal'.format(vilao.title()))


for i in range(1,10,2):
    print (i)

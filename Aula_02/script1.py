#!/usr/bin/python3
cores = {'red': 'vermelho','blue':'azul', 'green': 'verde', 'gold': 'dourado','silver':'prata'}
#print(cores)

koppa_red = {'color':'red', 'points':30}
koppa_blue = {'color': 'blue', 'points':50}
koppa_green = {'color':'green', 'points':10}

pontos = koppa_red['points']
#print('Você ganhhou {} pontos'.format(pontos))

###########################################################################################################

koppa_red['eixo_x'] = 5
koppa_red['eixo_y'] = 15
koppa_red['speed'] = 'rapido'

#print(koppa_red)

if koppa_red['speed'] == 'devegar':
	andar_x = 1
elif koppa_red['speed'] == 'medio':
	andar_x = 2
else:
	andar_x = 3

koppa_red['eixo_x'] += andar_x

#print('Posicao do koppa: {}'.format(koppa_red['eixo_x']))

###########################################################################################################

mago = {}
mago['cor'] = 'azul'
mago['pontos'] = 15
#print(mago)
mago['cor'] = 'verde'
#print(mago['cor'])
del mago['cor']
#print(mago)

###########################################################################################################

usuario = {'username':'dogjake', 'nome':'jake','sobrenome':'jake the dog'}

#for chave,valor in usuario.items():
	#print('chave: {}'.format(chave))
	#print('valor: {}'. format(valor))

#for chave in usuario.keys():
	#print('chave: {}'.format(chave))

#for valor in usuario.values():
	#print('valor: {}'.format(valor))

#for chave in sorted(usuario.keys()):
	#print('chave: {}'.format(chave))

koppa = []

#for k in range(10):
	#koppa.append(koppa_green)

#for tropa in koppa[:5]:
	#print(tropa)

###########################################################################################################

lanche = {'pao':['integral','4 queijos','italiano'],'queijo':['prato','cheddar','suico'],'recheio':['steak','frango','almondega']}

#print(lanche['pao'][2])

#for k,v in lanche.items():
	#print('{}: {}\n'.format(k,v[0]))

###########################################################################################################

herois = {'batman':{'nome': 'bruce wayne','cidade':'gotham'},'superman':{'nome':'clark kent','cidade':'metropolis'}}

print(herois['batman']['nome'])
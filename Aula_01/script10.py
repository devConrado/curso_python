data = input('Digite sua data de nascimento, no formato (dd/mm/aaaa): ')

data.split('/')
meses = ['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho','julho', 'agosto', 'setembro','outubro', 'novembro', 'dezembro']
print('Voce nasceu no dia: '+ data[0] + ' de ' + mes[int(meses) - 1] + ' de '+ data[2])

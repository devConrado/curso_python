idade =int(input('idade: '))
habilitado = input('possui habilitacao: ')

if habilitado.lower().strip() == 'sim' and idade >= 18:
    print ('Você pode dirigir')
else:
    print('Vocẽ não pode dirigir!')


exit()
velocidade = 110

if velocidade > 100:
    print ('você foi multado !')
else:
    print('não foi multado')

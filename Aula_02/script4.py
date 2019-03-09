#!/usr/bin/python3

while True:
	n1 = int(input('1o num: '))
	n2 = int(input('2o num: '))
	try:
		r = n1/n2
	except ZeroDivisionError as e:
		print(e)
	else:
		print(r)
	finally:
		print("fim")
exit()


#####################################################################################################
try:
	print(5/0)
except ZeroDivisionError as e:
	print(e)
else:
	pass
finally:
	pass
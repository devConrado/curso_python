#!/usr/bin/python3

import sys as s

print(s.argv)

for i in range(len(s.argv)):
	print('Parametro {}o : {}'.format(i,s.argv[i]))
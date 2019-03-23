#!/usr/bin/python3
from freq import frequencia
import random

while True:
	r = random.randint(263,529)
	frequencia(r)
	time.sleep(2)
	if r == 528:
		exit()
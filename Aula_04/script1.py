#!/usr/bin/python3

import random, time
import datetime
from subprocess import run, PIPE
import script2 as meu_modulo

r = run(['apt','install','-y','cowsay'],stdout=PIPE,stderr=PIPE)
alfabeto = 'abcdefghijklmnopqrstuvwxyz'

meu_modulo.retorna(r)
print(random.randint(100,999))
time.sleep(2)
print(random.randint(100,999))
time.sleep(2)
print(random.choice(alfabeto))
time.sleep(2)
print(random.choice(alfabeto))
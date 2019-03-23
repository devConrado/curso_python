
#!/usr/bin/python3

def quadrado(n):
    return n**2

def raiz(n):
    return n**0.5

funcs = [quadrado,raiz]

[print(list(map(lambda x : x(i), funcs)) for i in range(26))]

exit()

for i in range(26):
    valores = list(map(lambda x : x(i), funcs))
    print(valores)


exit()
num1 = [1,2,3]
num2 = [4,5,6]

r = list(map(lambda x,y : x * y,num1,num2))
print(r)

exit()

num = (1,2,3,4,5)
resultado = list(map(lambda x: x*2,num))
print(resultado)

exit()
def dobro(n):
    return 2 * n

num = (1,2,3,4,5)
resultado = list(map(dobro,num))

print(resultado)

exit()
import math as m

l1 = [1,4,9,16,25]
l2 = map(m.sqrt,l1)
print(list(l2))

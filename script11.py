pot = []

for valor in range(1,11):
	if valor %  2 == 0:
		pot.append(valor**2)

print(pot)

pot = [(valor ** 2) for valor in range(1,11) if valor % 2 == 0]
print(pot)
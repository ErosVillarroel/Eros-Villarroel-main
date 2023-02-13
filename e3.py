lista = [2,8,6,7,14,15]

n = input('Por favor ingrese un n para la lista: \n')
while not n.isnumeric() or int(n) not in range(1,len(lista)+1):
    n = input('Por favor ingrese un numero valido: \n')

n = int(n)
aux1 = []
aux2 = []
counter = 0
for i in range(0, n+1):
    aux1.append(lista[i])

for h in range(0, (len(lista)-n)):
    aux2.append(lista[h+n])

aux1.sort()
aux2.sort()

aux3 = set(aux1+aux2)
print(list(aux3))

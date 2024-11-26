primero = {1, 1, 2, 2, 3, 4}
print(primero)

numeros = list(primero)
print(numeros)

list = [3, 4, 5]

segundo = set(list)
print(segundo)

print("|", primero | segundo)
print("&", primero & segundo)
print("-", primero - segundo)

numeros = (1, 2, 3) + (4, 5, 6)
print(numeros)

punto = tuple([1, 2])
print(punto)

menosNumeros = numeros[:4]
print(menosNumeros)

primero, segundo, *otros = numeros
print(primero, segundo, otros)

for n in numeros:
    print(n)

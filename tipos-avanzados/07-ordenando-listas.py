numeros = [2, 1, 5, 20, 15, 54, 32]

numeros.sort(reverse=True)
print(numeros)
numeros2 = sorted(numeros)
print(numeros2)

usuarios = [
    ["Chanchito", 1],
    ["Feliz", 4],
    ["Fresa", 2]
]

usuarios.sort(key=lambda el: el[1])
print("usuarios", usuarios)

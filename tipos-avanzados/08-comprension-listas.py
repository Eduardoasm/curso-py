usuarios = [
    ["Chanchito", 1],
    ["Feliz", 4],
    ["Fresa", 2]
]

# nombres = [usuario[0] for usuario in usuarios]

# print("nombres", nombres)

# nombreFilter = [usuario for usuario in usuarios if usuario[1] >= 2]
# print("nombreFilter", nombreFilter)

nombres = list(map(lambda usuario: usuario[0], usuarios))
print("nombres", nombres)


menosUsarios = list(filter(lambda usuario: usuario[1] >= 2, usuarios))
print("menosUusarios", menosUsarios)

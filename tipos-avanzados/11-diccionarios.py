diccionario = {"x": 30, "y": 50}

diccionario["z"] = 60

print(diccionario)

for valor in diccionario:
    print(valor, diccionario[valor])

for llave, prop in diccionario.items():
    print(prop)

usuarios = [
    {
        "id": "123",
        "name": "Chanchito"
    },
    {
        "id": "123",
        "name": "Feliz"
    },
    {
        "id": "123",
        "name": "Dog"
    },
]

for usuario in usuarios:
    print(usuario["name"])

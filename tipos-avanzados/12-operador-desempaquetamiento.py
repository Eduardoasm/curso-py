punto1 = {"x": 10, "y": 20}
punto2 = {"y": 32}

punto3 = {**punto1, "z": "hola mundo", **punto2}

print(punto3)

def hola(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


hola(10, 2, 13)
hola(3, 45, 32, 15)
hola(1, 2, 6, 23, 31, 44)

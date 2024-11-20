n1 = input("Indique el primer numero")
n2 = input("Indique el segundo numero")

n1 = int(n1)
n2 = int(n2)

suma = n1 + n2
resta = n1 - n2
mult = n1 * n2
div = n1 / n2

descripcion = f"""
el resultado de los 2 numeros de {n1} y {n2}
el resultado de la suma es {suma}
el resultado de la resta es {resta}
el resultado de la multiplicación es {mult}
el resultado de la división es {div}
"""

print(descripcion)

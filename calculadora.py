print("Bienvenidos a la calculadora")
print("Para salir escribir Salir")
print("las operaciones son suma, multi, div y resta")
# n1 = input(" Escriba un numero: ")
# n1 = int(n1)
resultado = ""


while True:
    if not resultado:
        resultado = input("Ingresa un numero: ")
        if resultado.lower == "salir":
            break
        resultado = int(resultado)
    op = input("Ingresa una operacion: ")
    if op.lower() == "salir":
        break
    n2 = input("Ingresa el siguiente numero: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)
    if op == "suma":
        resultado += n2
    elif op == "resta":
        resultado -= n2
    elif op == "div":
        resultado /= n2
    elif op == "multi":
        resultado *= n2
    else:
        print("Operacion no valida")
    print(f"El resultado es {resultado}")

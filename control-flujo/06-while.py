comando = ""

# while comando != "salir":
#     comando = input("$ ")
#     print(comando)

comando = ""
while True:
    comando = input("$ ")
    print(comando)
    if comando.lower() == "salir":
        break

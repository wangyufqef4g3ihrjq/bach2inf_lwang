def ocho():
    lista = []
    for nombre in range (0,5):
        nombre=input("Introduce un nombre --> ")
        lista.append(nombre)
    lista.reverse()
    print("Lista de nombres introducidos en inverso: ")
    for nombre in lista:
        print(nombre)
ocho()

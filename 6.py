def seis():
    numero = int(0)
    while True:
        num=int(input("Introduce un número(0 para terminar): "))
        if num == 0:
            break
        numero = numero + num
    print(str("La suma de los números es: ")+ str(numero))
seis()

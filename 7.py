def siete():
    lista=[4.5,7,3,9.5,6,8,5]
    print(str("La nota máxima: ")+ str(max(lista)))
    print(str("La nota mínimo: ")+ str(min(lista)))
    media= (sum(lista)/7)
    print(str("La nota media es: ")+ str(round(media,2)))
    for n in lista:
        if n >= 5 in lista:
            print(str(n)+" = Aprobado")
        else:
            print(str(n)+" = Suspendido")
        
siete()

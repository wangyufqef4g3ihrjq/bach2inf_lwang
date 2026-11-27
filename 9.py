def nueve():
    dias=("Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo",)
    num=int(input("Dame un número del 1 al 7: "))
    if 1 <= num <= 7:
        print(dias[num-1])
    else:
        print("NÚMERO INVÁLIDO")
nueve()
    

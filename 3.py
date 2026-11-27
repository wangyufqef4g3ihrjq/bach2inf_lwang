def tres():
    nota=float(input("Dame una nota del 1 al 10 con dos decimales -->"))
    if nota < 5:
        print("menor que 5")
    elif 5 <= nota <= 6.99:
        print("5 a 6.99")
    elif 7 <= nota <= 8.99:
        print("7 a 8.99")
    else:
        print("9 o más")
        
tres()

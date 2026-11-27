def cuatro():

    año = int(input("Introduce un año: "))
    if (año % 4 == 0 or año % 400 == 0) and año % 100 != 0:
            print("bisiesto")
    else:
            print("no bisiesto")
cuatro()

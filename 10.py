def diez():
    dic={"España":"Madrid","Francia":"París","Alemania":"Berlín","Portugal":"Lisboa"}
    pais=input("Dame un país: ")
    capital=dic[pais]
    print("La capital del país introducido es: "+ str(capital))
    if pais == "España" and pais == "Francia" and pais == "Alemania" and pais == "Portugal":
        print("La capital del país introducido es: "+ str(capital))
    else:
        print("El país introducido no esta incluido")
diez()

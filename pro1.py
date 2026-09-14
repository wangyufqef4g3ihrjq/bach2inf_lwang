def programa_1():
    x='a'                  #variable tipo caracter (CHARACTER char)
    edad=17                #variable tipo entero (INTEGER o INT)
    pi=3.14                #variable tipo decimal (FLOAT o DOUBLE)
    na=2.7e23              #variable exponencial (DOUBLE)
    respuesta=True #variable tipo booleana
    entradilla1="Dame un número = "
    entradilla2="Dame otro número = "
    mensaje="La suma vale " #Es un STRING
    num1=int(input(entradilla1))   #num1 es una variable
    num2=int(input(entradilla2)) #num2 es una variable
    print(mensaje+str(num1+num2))

programa_1()

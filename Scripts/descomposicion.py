import sys

if len(sys.argv)==2:
    numero = int(sys.argv[1])

    if numero < 0 or numero > 9999:
        print("Error - Numero es Incorrectos")
        print("Ejemplo: tabla.py [1-9] [1-9]")
    else:
        # Aqui va la logica
        cadena = str(numero)
        longitud = len(cadena)

        for i in range(longitud):
            print("{:04d}".format(int(cadena[longitud-1-i]) * 10**i))
else:
    print("Error - Argumentos Incorrectos")
    print("Ejemplo: descomposicion.py [0-9999]")
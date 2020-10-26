#P3 E5 - rgion
#Pida un número que como máximo tenga tres cifras
#(por ejemplo serían válidos 1, 99 i 213 pero no 1001). Si el usuario introduce
#un número de más de tres cifras debe un informar con un mensaje de error
#como este “ ERROR: El número 1005 tiene más de tres cifras”

numero=int(input("Introduzca un número de como máximo 3 cifras"))
if (numero>=1000):
    print("ERROR. El número introducido es mayor de 3 cifras")

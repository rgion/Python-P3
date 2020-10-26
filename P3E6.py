#P3 E6 - rgion
#Pida al usuario el precio de un producto y el nombre del producto y muestre
# el mensaje con el precio del IVA (21%). Por ejemplo: “ Tu bicicleta vale
# 100 euros y con el 21 % de IVA se queda en 121 euros en total”.

precio=float(input("Introduzca el precio del producto"))
nombre=input("Introduzca el nombre del producto")
precioIVA=float((precio*0.21)+precio)
print("Tu", nombre, "vale" ,precio, "y con el 21 % de IVA se queda en" ,precioIVA, "en total")

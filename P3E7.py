#P3 E7 - rgion
#Pida al usuario tres número que serán el día, mes y año. Comprueba
#que la fecha introducida es válida.  Por ejemplo: 
#32/01/2017->Fecha incorrecta
#29/02/2017->Fecha incorrecta
#30/09/2017->Fecha correcta.
dia=int(input("Introduzca el día "))
mes=int(input("Introduzca el mes "))
año=int(input("Introduzca el año "))
if (dia>31)or(dia<=0)or(mes>12)or(mes<=0)or(año<=0):
    print(dia,"/",mes,"/",año, "->Fecha incorrecta")
elif (mes==2 and dia>28)or(mes==4 and dia>30)or(mes==6 and dia>30)or(mes==9 and dia>30)or(mes==11 and dia>30):
    print(dia,"/",mes,"/",año, "->Fecha incorrecta")
else:
    print(dia,"/",mes,"/",año, "->Fecha correcta")


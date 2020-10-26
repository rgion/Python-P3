#P3 E2 - rgion
#Pida al usuario el espacio recorrido por un coche y el tiempo que ha tardado
#en horas y que calcule a qué velocidad media había realizado el recorrido.

espacio=float(input("Introduzca espacio en metros recorrido por el coche"))
hora=int(input("Introduzca el tiempo en horas que ha tardado en recorrer esta distancia"))
velocidad=float((espacio/1000)/hora)
print("El coche ha realizado el recorrido en", velocidad, "Km/h")

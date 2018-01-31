from boletin8 import convertir_a_euros
tarifa=float(input("¿Cual es tu tarifa en centimos por segundo? "))
com=int(input("¿Cuantas comunicaciones se han realizado? "))
cont=0
while cont != com:
	segundos=int(input("¿Cuantas segundos duró? "))
	minutos=int(input("¿Cuantas minutos duró? "))
	horas=int(input("¿Cuantas horas duró? "))
	print("La comunicación nº%d costó"%cont,result)
	result=convertir_a_euros(horas,minutos,segundos,tarifa)
	cont+=1
from boletin8 import convertir_a_euros,calcular_coste,pasar_a_segundos
tarifa=float(input("¿Cual es tu tarifa en centimos por segundo? "))
com=int(input("¿Cuantas comunicaciones se han realizado? "))
cont=0
while cont != com:
	segundos=int(input("¿Cuantas segundos duró? "))
	minutos=int(input("¿Cuantas minutos duró? "))
	horas=int(input("¿Cuantas horas duró? "))
	print("La comunicación nº%d costó"%(cont+1),end=" ")
	result=convertir_a_euros(horas,minutos,segundos,tarifa)
	print(result)
	cont+=1
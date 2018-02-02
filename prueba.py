from boletin8 import convertir_a_euros,pasar_a_segundos
tarifa=float(input("¿Cual es tu tarifa en centimos por segundo? "))
com=int(input("¿Cuantas comunicaciones se han realizado? "))
cont=0
while cont != com:
	s=int(input("¿Cuantas segundos duró? "))
	m=int(input("¿Cuantas minutos duró? "))
	h=int(input("¿Cuantas horas duró? "))
	euros,cent=convertir_a_euros(pasar_a_segundos(h,m,s),tarifa)
	print("La comunicación nº%d costó %d euros y %d centimos"%((cont+1),euros,cent))
	cont+=1